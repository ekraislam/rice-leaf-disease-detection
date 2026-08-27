import os
import io
import base64
import traceback
from flask import Flask, render_template, request, jsonify, send_from_directory, Response
import torch
from torchvision import transforms
from PIL import Image, UnidentifiedImageError
from src.model import get_baseline_cnn
from src.disease_data import DISEASE_DATABASE
from src.gradcam import GradCAM

# ── PyTorch Thread Optimization ──────────────────────────────────────────────
# Use env var TORCH_THREADS to override. Default: min(2, cpu_count).
# On Render free tier (0.1 vCPU shared), 2 is a safe practical ceiling.
_cpu_count = os.cpu_count() or 1
_torch_threads = int(os.environ.get("TORCH_THREADS", str(min(2, _cpu_count))))
torch.set_num_threads(_torch_threads)
torch.set_grad_enabled(False)          # global no-grad by default (re-enabled only for Grad-CAM)

app = Flask(__name__)

# Enforce 50 MB maximum upload file size limit (allows up to 25 batch photos)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024
app.config['TEMPLATES_AUTO_RELOAD'] = True

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "fair_augmented_cnn.pth")

CLASS_NAMES = [
    "Bacterial Leaf Blight",
    "Brown Spot",
    "Healthy Rice Leaf",
    "Leaf Blast",
    "Leaf scald",
    "Narrow Brown Leaf Spot",
    "Rice Hispa",
    "Sheath Blight",
]

EXPECTED_CLASSES = [
    "Bacterial Leaf Blight",
    "Brown Spot",
    "Healthy Rice Leaf",
    "Leaf Blast",
    "Leaf scald",
    "Narrow Brown Leaf Spot",
    "Rice Hispa",
    "Sheath Blight",
]

device = torch.device("cpu")

model = get_baseline_cnn(num_classes=8, pretrained=False)
if os.path.exists(MODEL_PATH):
    state_dict = torch.load(MODEL_PATH, map_location=device, weights_only=True)
    model.load_state_dict(state_dict)
for p in model.parameters():
    p.requires_grad = False
model.to(device)
model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    ),
])

# ── Model Warm-up ─────────────────────────────────────────────────────────────
# Run a dummy inference at startup so the first real request is not cold.
try:
    _dummy = torch.zeros(1, 3, 224, 224, device=device)
    with torch.no_grad():
        model(_dummy)
    del _dummy
    print("[RiceGuard] Model warm-up complete.")
except Exception as _warm_err:
    print(f"[RiceGuard] Warm-up warning: {_warm_err}")

# ── Persistent GradCAM instance (reuse hooks across requests) ─────────────────
_gcam = GradCAM(model)

print(f"[RiceGuard] Starting — threads={_torch_threads}, device={device}")


@app.errorhandler(413)
def request_entity_too_large(error):
    msg = "File size exceeds the maximum allowed limit of 10 MB. Please select a smaller rice leaf image."
    is_ajax = (
        request.headers.get("X-Requested-With") == "XMLHttpRequest"
        or "application/json" in request.headers.get("Accept", "")
        or request.args.get("ajax") == "1"
    )
    if is_ajax:
        return jsonify({"success": False, "error": msg}), 413
    return render_template(
        "index.html",
        prediction=None,
        confidence=None,
        top_predictions=None,
        disease_info=None,
        expected_class=None,
        error=msg,
        CLASS_NAMES=CLASS_NAMES,
        EXPECTED_CLASSES=EXPECTED_CLASSES,
        DISEASE_DATABASE=DISEASE_DATABASE
    ), 413


from werkzeug.exceptions import HTTPException


@app.errorhandler(Exception)
def handle_unexpected_error(error):
    if isinstance(error, HTTPException):
        return error
    traceback.print_exc()
    msg = f"Inference error: {str(error)}"
    is_ajax = (
        request.headers.get("X-Requested-With") == "XMLHttpRequest"
        or "application/json" in request.headers.get("Accept", "")
        or request.args.get("ajax") == "1"
    )
    if is_ajax:
        return jsonify({"success": False, "error": msg}), 500
    return render_template(
        "index.html",
        prediction=None,
        confidence=None,
        top_predictions=None,
        disease_info=None,
        expected_class=None,
        error=msg,
        CLASS_NAMES=CLASS_NAMES,
        EXPECTED_CLASSES=EXPECTED_CLASSES,
        DISEASE_DATABASE=DISEASE_DATABASE
    ), 500


def run_inference_on_pil_image(image, expected_class=None, generate_cam=True):
    """
    Runs single-pass inference and Grad-CAM on a PIL image.
    Returns a dict with prediction details.
    """
    image_tensor = transform(image).unsqueeze(0).to(device)
    cam_input = image_tensor.requires_grad_(True)

    with torch.enable_grad():
        outputs = model(cam_input)
        probabilities = torch.softmax(outputs.detach(), dim=1)[0]
        confidence_val, predicted_idx = torch.max(probabilities, dim=0)

        # Top-3 predictions
        top_probs, top_indices = torch.topk(probabilities, k=min(3, len(CLASS_NAMES)))
        top_predictions = []
        for p, idx in zip(top_probs, top_indices):
            c_name = CLASS_NAMES[idx.item()]
            c_info = DISEASE_DATABASE.get(c_name, {})
            top_predictions.append({
                "class": c_name,
                "class_bn": c_info.get("name_bn", c_name),
                "confidence": round(p.item() * 100, 2),
                "severity_en": c_info.get("severity_en", "Moderate"),
                "severity_bn": c_info.get("severity_bn", "মাঝারি"),
                "severity_color": c_info.get("severity_color", "#10B981")
            })

        prediction = CLASS_NAMES[predicted_idx.item()]
        confidence = round(confidence_val.item() * 100, 2)
        disease_info = DISEASE_DATABASE.get(prediction, {})
        gradcam_url = None

        if generate_cam and _gcam is not None:
            try:
                cam_map = _gcam.generate_from_logits(outputs, class_idx=predicted_idx.item())
                if cam_map is not None:
                    gradcam_url = _gcam.overlay_heatmap(image, cam_map, alpha=0.5)
            except Exception as gcam_err:
                print("Grad-CAM generation warning:", gcam_err)
                _gcam.activations = None
                _gcam.gradients = None

        return {
            "prediction": prediction,
            "confidence": confidence,
            "top_predictions": top_predictions,
            "disease_info": disease_info,
            "gradcam_url": gradcam_url,
            "expected_class": expected_class if expected_class else None
        }


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    confidence = None
    top_predictions = None
    disease_info = None
    expected_class = None
    gradcam_url = None
    error = None

    if request.method == "POST":
        expected_class = request.form.get("expected_class", "").strip()
        if "image" not in request.files:
            error = "Please select a rice leaf image to analyze."
        else:
            file = request.files["image"]

            if not file or file.filename == "":
                error = "Please select a rice leaf image to analyze."
            else:
                try:
                    image = Image.open(file).convert("RGB")
                    result = run_inference_on_pil_image(image, expected_class=expected_class, generate_cam=True)
                    prediction = result["prediction"]
                    confidence = result["confidence"]
                    top_predictions = result["top_predictions"]
                    disease_info = result["disease_info"]
                    gradcam_url = result["gradcam_url"]
                except UnidentifiedImageError:
                    error = "We couldn't read this image file. Please upload a valid image (JPG, PNG, BMP, or TIFF)."
                except Exception as e:
                    error = f"Analysis failed: {str(e)}"
                    traceback.print_exc()

        # Check if the request is an AJAX call from the frontend
        is_ajax = (
            request.headers.get("X-Requested-With") == "XMLHttpRequest"
            or "application/json" in request.headers.get("Accept", "")
            or request.args.get("ajax") == "1"
        )
        if is_ajax:
            if error:
                return jsonify({
                    "success": False,
                    "error": error
                }), 400
            return jsonify({
                "success": True,
                "prediction": prediction,
                "confidence": confidence,
                "top_predictions": top_predictions,
                "disease_info": disease_info,
                "gradcam_url": gradcam_url,
                "expected_class": expected_class if expected_class else None,
                "error": None
            })

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        top_predictions=top_predictions,
        disease_info=disease_info,
        expected_class=expected_class,
        gradcam_url=gradcam_url,
        error=error,
        expected_classes=EXPECTED_CLASSES,
        EXPECTED_CLASSES=EXPECTED_CLASSES,
        DISEASE_DATABASE=DISEASE_DATABASE,
        all_diseases=DISEASE_DATABASE
    )


@app.route("/api/batch-predict", methods=["POST"])
def batch_predict():
    """
    Multi-Image Batch Field Health Audit Endpoint.
    Analyzes up to 25 leaves sampled across a field and computes aggregate health indices,
    visual disease breakdown, integrated combined prescription, and audio narration.
    """
    uploaded_files = request.files.getlist("files") or request.files.getlist("images")
    if not uploaded_files or len(uploaded_files) == 0:
        return jsonify({"success": False, "error": "No image files uploaded for batch analysis."}), 400

    if len(uploaded_files) > 25:
        uploaded_files = uploaded_files[:25]  # Cap at 25 images

    samples = []
    class_counts = {}
    total_valid = 0

    for idx, f in enumerate(uploaded_files):
        if not f or f.filename == "":
            continue
        try:
            pil_img = Image.open(f).convert("RGB")
            # Generate small base64 thumbnail for grid display
            thumb = pil_img.copy()
            thumb.thumbnail((320, 320))
            buffered = io.BytesIO()
            thumb.save(buffered, format="JPEG", quality=85)
            thumb_b64 = "data:image/jpeg;base64," + base64.b64encode(buffered.getvalue()).decode("utf-8")

            res = run_inference_on_pil_image(pil_img, generate_cam=True)
            pred = res["prediction"]
            d_info = res["disease_info"]

            total_valid += 1
            class_counts[pred] = class_counts.get(pred, 0) + 1

            samples.append({
                "id": idx + 1,
                "filename": f.filename or f"Sample_{idx+1}.jpg",
                "thumb_url": thumb_b64,
                "prediction": pred,
                "name_bn": d_info.get("name_bn", pred),
                "name_en": d_info.get("name_en", pred),
                "confidence": res["confidence"],
                "severity_bn": d_info.get("severity_bn", "সতর্কতা"),
                "severity_en": d_info.get("severity_en", "Caution"),
                "severity_color": d_info.get("severity_color", "#10B981"),
                "gradcam_url": res["gradcam_url"],
                "top_predictions": res["top_predictions"],
                "symptoms_bn": d_info.get("symptoms_bn", []),
                "symptoms_en": d_info.get("symptoms_en", []),
                "chemical_bn": d_info.get("management_bn", {}).get("chemical", ""),
                "chemical_en": d_info.get("management_en", {}).get("chemical", ""),
                "cultural_bn": d_info.get("management_bn", {}).get("cultural", ""),
                "cultural_en": d_info.get("management_en", {}).get("cultural", "")
            })
        except Exception as e:
            print(f"Skipping invalid batch image {getattr(f, 'filename', 'unknown')}: {e}")

    if total_valid == 0:
        return jsonify({"success": False, "error": "Could not process any of the uploaded images. Please upload valid JPG/PNG files."}), 400

    # ── Aggregate Field Analytics ──────────────────────────────
    healthy_count = class_counts.get("Healthy Rice Leaf", 0)
    healthy_pct = round((healthy_count / total_valid) * 100, 1)

    disease_breakdown = []
    for c_name, cnt in sorted(class_counts.items(), key=lambda x: x[1], reverse=True):
        c_info = DISEASE_DATABASE.get(c_name, {})
        pct = round((cnt / total_valid) * 100, 1)
        disease_breakdown.append({
            "class_name": c_name,
            "name_bn": c_info.get("name_bn", c_name),
            "name_en": c_info.get("name_en", c_name),
            "count": cnt,
            "percentage": pct,
            "severity_bn": c_info.get("severity_bn", "মাঝারি"),
            "severity_en": c_info.get("severity_en", "Moderate"),
            "severity_color": c_info.get("severity_color", "#10B981"),
            "is_healthy": (c_name == "Healthy Rice Leaf")
        })

    # Dominant condition
    dominant_class = disease_breakdown[0]["class_name"]
    dominant_info = DISEASE_DATABASE.get(dominant_class, {})

    # Determine overall field health risk level
    diseased_pct = 100.0 - healthy_pct
    if healthy_pct >= 85:
        field_risk = {
            "level_bn": "সুস্থ ও নিরাপদ (Excellent)",
            "level_en": "Healthy & Safe (Excellent)",
            "badge_class": "risk-healthy",
            "color": "#10B981",
            "desc_bn": "জমির সিংহভাগ পাতা সম্পূর্ণ সুস্থ। কোনো রাসায়নিক স্প্রে করার প্রয়োজন নেই। সুষম সার ও সেচ ব্যবস্থাপনা বজায় রাখুন।",
            "desc_en": "Overwhelming majority of crop samples are healthy. No pesticide spray required. Maintain balanced irrigation."
        }
    elif diseased_pct <= 30:
        field_risk = {
            "level_bn": "প্রাথমিক সতর্কতা (Low Caution)",
            "level_en": "Early Caution (Low Risk)",
            "badge_class": "risk-low",
            "color": "#F59E0B",
            "desc_bn": "মাঠে প্রাথমিক সংক্রমণের উপস্থিতি পাওয়া গেছে। দ্রুত রোগাক্রান্ত অংশ পর্যবেক্ষণ করুন এবং স্প্রে করার প্রস্তুতি নিন।",
            "desc_en": "Early stage localized infection detected. Monitor hotspots and prepare preventive spraying if conditions favor spread."
        }
    elif diseased_pct <= 60:
        field_risk = {
            "level_bn": "মাঝারি সংক্রমণ (Moderate Alert)",
            "level_en": "Moderate Alert (Action Needed)",
            "badge_class": "risk-medium",
            "color": "#EA580C",
            "desc_bn": "মাঠের উল্লেখযোগ্য অংশে রোগ ছড়িয়ে পড়ছে। জমিতে অবিলম্বে প্রস্তাবিত সমন্বিত বালাইনাশক স্প্রে করুন।",
            "desc_en": "Significant disease presence across the plot. Immediate integrated spray application recommended."
        }
    else:
        field_risk = {
            "level_bn": "উচ্চ ঝুঁকি ও মহামারী আশঙ্কা (High Outbreak)",
            "level_en": "High Outbreak Risk (Severe Alert)",
            "badge_class": "risk-high",
            "color": "#DC2626",
            "desc_bn": "জমির অধিকাংশ নমুনায় তীব্র রোগের আক্রমণ দেখা গেছে। জরুরি ভিত্তিতে ওষুধ স্প্রে ও ইউরিয়া সার প্রয়োগ স্থগিত রাখুন।",
            "desc_en": "High epidemic pressure across field samples. Emergency spray intervention required immediately; suspend top-dressing Nitrogen."
        }

    # ── Integrated Master Prescription ────────────────────────
    active_diseases = [d for d in disease_breakdown if not d["is_healthy"]]

    if len(active_diseases) == 0:
        master_prescription = {
            "chemical_bn": "জমিতে কোনো রাসায়নিক বালাইনাশক বা ছত্রাকনাশক স্প্রে করার প্রয়োজন নেই। ফসল সম্পূর্ণ সুস্থ ও সতেজ রয়েছে।",
            "chemical_en": "No chemical pesticide or fungicide spray required. Crops are healthy and vigorous.",
            "cultural_bn": "জমিতে পরিমিত পানি রাখুন, আগাছা মুক্ত রাখুন এবং অনুমোদিত মাত্রায় সুষম সার (ইউরিয়া, টিএসপি, এমওপি) প্রয়োগ করুন।",
            "cultural_en": "Maintain standing irrigation, keep plots weed-free, and apply balanced fertilizers according to crop growth stage.",
            "fertilizer_advisory_bn": "সার প্রয়োগের স্বাভাবিক নিয়ম বজায় রাখুন। অতিরিক্ত ইউরিয়া পরিহার করুন।",
            "fertilizer_advisory_en": "Follow normal fertilizer schedule. Avoid excessive nitrogen/urea."
        }
    elif len(active_diseases) == 1:
        single_d = DISEASE_DATABASE.get(active_diseases[0]["class_name"], {})
        master_prescription = {
            "chemical_bn": single_d.get("management_bn", {}).get("chemical", ""),
            "chemical_en": single_d.get("management_en", {}).get("chemical", ""),
            "cultural_bn": single_d.get("management_bn", {}).get("cultural", ""),
            "cultural_en": single_d.get("management_en", {}).get("cultural", ""),
            "fertilizer_advisory_bn": "রোগাক্রান্ত অবস্থায় ইউরিয়া সার প্রয়োগ সাময়িক বন্ধ রাখুন এবং প্রতি বিঘায় ৫ কেজি অতিরিক্ত পটাশ সার ব্যবহার করুন।",
            "fertilizer_advisory_en": "Suspend urea application temporarily during active infection and apply 5 kg/bigha supplemental Potash."
        }
    else:
        # Multiple co-occurring diseases: combine chem & cultural
        chem_parts_bn = []
        chem_parts_en = []
        for ad in active_diseases:
            d_data = DISEASE_DATABASE.get(ad["class_name"], {})
            chem_parts_bn.append(f"• {ad['name_bn']}: {d_data.get('management_bn', {}).get('chemical', '')}")
            chem_parts_en.append(f"• {ad['name_en']}: {d_data.get('management_en', {}).get('chemical', '')}")

        master_prescription = {
            "chemical_bn": "\n".join(chem_parts_bn),
            "chemical_en": "\n".join(chem_parts_en),
            "cultural_bn": "একাধিক রোগের বিস্তার রোধে আক্রান্ত জমির পানি অন্য জমিতে প্রবাহিত হতে দেবেন না। মাঠের আগাছা পরিষ্কার করুন ও বিকেলে স্প্রে করুন।",
            "cultural_en": "To prevent multi-disease spread, prevent drainage runoff between plots. Weed borders and spray in calm late afternoon.",
            "fertilizer_advisory_bn": "জরুরি সতর্কতা: নাইট্রোজেন/ইউরিয়া সার পুরোপুরি বন্ধ রাখুন। গাছের রোগ প্রতিরোধ ক্ষমতা বাড়াতে পটাশ (MOP) ও জিংক প্রয়োগ করুন।",
            "fertilizer_advisory_en": "Critical: Suspend Nitrogen/Urea immediately. Apply Potash (MOP) and Zinc to boost crop resistance."
        }

    # ── Speech Summary Script Generation ──────────────────────
    if healthy_pct >= 85:
        speech_text_bn = f"মাঠ নিরীক্ষা সম্পন্ন হয়েছে। মোট {total_valid}টি পাতার নমুনার মধ্যে শতকরা {healthy_pct} ভাগ পাতা সম্পূর্ণ সুস্থ। সার্বিক মাঠের স্বাস্থ্য অত্যন্ত চমৎকার। জমিতে কোনো রাসায়নিক স্প্রে করার প্রয়োজন নেই।"
        speech_text_en = f"Field health audit complete. Out of {total_valid} leaf samples, {healthy_pct} percent are completely healthy. Field condition is excellent. No chemical spray is required."
    elif len(active_diseases) == 1:
        d_name_bn = active_diseases[0]["name_bn"]
        d_name_en = active_diseases[0]["name_en"]
        d_pct = active_diseases[0]["percentage"]
        speech_text_bn = f"মাঠ নিরীক্ষায় {total_valid}টি নমুনার মধ্যে শতকরা {healthy_pct} ভাগ সুস্থ এবং {d_pct} ভাগ পাতায় {d_name_bn} পাওয়া গেছে। মাঠের সার্বিক অবস্থা {field_risk['level_bn']}। প্রস্তাবিত প্রেসক্রিপশন: {master_prescription['chemical_bn']}"
        speech_text_en = f"Field audit completed across {total_valid} samples. {healthy_pct} percent are healthy and {d_pct} percent show {d_name_en}. Overall field risk is {field_risk['level_en']}. Recommended management: {master_prescription['chemical_en']}"
    else:
        disease_summary_bn = " এবং ".join([f"{ad['percentage']}% {ad['name_bn']}" for ad in active_diseases])
        disease_summary_en = " and ".join([f"{ad['percentage']}% {ad['name_en']}" for ad in active_diseases])
        speech_text_bn = f"মাঠ নিরীক্ষা রিপোর্ট: মোট {total_valid}টি নমুনার মধ্যে {healthy_pct}% পাতা সুস্থ। তবে জমিতে একাধিক রোগের সংক্রমণ দেখা গেছে: {disease_summary_bn}। সার্বিক মাঠ ঝুঁকি: {field_risk['level_bn']}। বিস্তারিত সমন্বিত বালাইনাশক প্রেসক্রিপশন স্ক্রিনে লক্ষ্য করুন।"
        speech_text_en = f"Field audit report: Across {total_valid} leaf samples, {healthy_pct}% are healthy. Multiple co-infections detected: {disease_summary_en}. Overall field risk is {field_risk['level_en']}. Please review the master prescription on screen."

    return jsonify({
        "success": True,
        "total_samples": total_valid,
        "healthy_count": healthy_count,
        "healthy_pct": healthy_pct,
        "disease_breakdown": disease_breakdown,
        "dominant_disease": {
            "class_name": dominant_class,
            "name_bn": dominant_info.get("name_bn", dominant_class),
            "name_en": dominant_info.get("name_en", dominant_class),
            "count": disease_breakdown[0]["count"],
            "percentage": disease_breakdown[0]["percentage"]
        },
        "field_risk": field_risk,
        "master_prescription": master_prescription,
        "speech_text_bn": speech_text_bn,
        "speech_text_en": speech_text_en,
        "samples": samples
    })

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        top_predictions=top_predictions,
        disease_info=disease_info,
        gradcam_url=gradcam_url,
        expected_class=expected_class,
        error=error,
        CLASS_NAMES=CLASS_NAMES,
        EXPECTED_CLASSES=EXPECTED_CLASSES,
        DISEASE_DATABASE=DISEASE_DATABASE
    )



from flask import Response
from src.tts_engine import generate_speech_audio, start_background_cache_prewarm
start_background_cache_prewarm()


@app.route("/api/tts", methods=["GET"])
def text_to_speech():
    disease = request.args.get("disease", "").strip()
    text = request.args.get("text", "").strip()
    lang = request.args.get("lang", "bn").strip().lower()
    voice = request.args.get("voice", "").strip().lower()
    gender = request.args.get("gender", "").strip().lower()

    lang_code = "bn" if lang.startswith("bn") else "en"

    # Determine gender preference
    if not gender:
        if voice in ["nabanita", "tanishaa", "aria", "jenny", "female"]:
            gender = "female"
        else:
            gender = "male"

    # 1. Instant Static Serving for Disease Audio (0ms Latency)
    if disease:
        slug = disease.lower().replace(" ", "_")
        candidate_files = [
            f"{slug}_{lang_code}_{gender}.mp3",
            f"{slug}_{lang_code}_{voice}.mp3" if voice else None,
            f"{slug}_{lang_code}.mp3"
        ]
        for fname in candidate_files:
            if not fname:
                continue
            audio_path = os.path.join(BASE_DIR, "static", "audio", fname)
            if os.path.exists(audio_path):
                with open(audio_path, "rb") as f:
                    return Response(
                        f.read(),
                        mimetype="audio/mpeg",
                        headers={
                            "Cache-Control": "public, max-age=86400",
                            "Accept-Ranges": "bytes"
                        }
                    )

    if not text:
        return jsonify({"error": "No text provided"}), 400

    try:
        resolved_voice = voice or ("pradeep" if gender == "male" else "nabanita")
        audio_bytes = generate_speech_audio(text=text, lang=lang_code, voice=resolved_voice, gender=gender)
        if audio_bytes and len(audio_bytes) > 200:
            return Response(
                audio_bytes,
                mimetype="audio/mpeg",
                headers={
                    "Cache-Control": "public, max-age=86400",
                    "Accept-Ranges": "bytes"
                }
            )
        return jsonify({"error": "TTS synthesis produced empty audio"}), 500
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": f"TTS generation failed: {str(e)}"}), 500


from src.agri_ai import query_agri_assistant


@app.route("/api/chat", methods=["POST"])
def chat_with_agri_ai():
    try:
        data = request.get_json(silent=True) or {}
        message = str(data.get("message") or "").strip()
        lang = str(data.get("lang") or "bn").strip()
        current_disease = data.get("current_disease")
        if isinstance(current_disease, str):
            current_disease = current_disease.strip() or None
        else:
            current_disease = None
        current_confidence = data.get("current_confidence", None)

        if not message:
            return jsonify({
                "success": False,
                "error": "No message provided"
            }), 400

        result = query_agri_assistant(
            message=message,
            lang=lang,
            current_disease=current_disease,
            current_confidence=current_confidence
        )

        return jsonify({
            "success": True,
            "html": result.get("html", ""),
            "text_bn": result.get("text_bn", ""),
            "text_en": result.get("text_en", ""),
            "source": result.get("source", "expert_system")
        })
    except Exception as e:
        traceback.print_exc()
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


from src.weather_service import get_live_weather, BANGLADESH_DISTRICTS
from src.outbreak_service import get_outbreak_map_data, record_outbreak_case


@app.route("/api/weather", methods=["GET"])
def get_weather_advisory():
    district = request.args.get("district", "").strip() or None
    lat_str = request.args.get("lat")
    lon_str = request.args.get("lon")
    try:
        lat = float(lat_str) if lat_str else None
        lon = float(lon_str) if lon_str else None
    except ValueError:
        lat, lon = None, None

    result = get_live_weather(district_name=district, lat=lat, lon=lon)
    return jsonify(result)


@app.route("/api/outbreak-map", methods=["GET"])
def get_outbreak_data():
    disease_filter = request.args.get("disease", "all").strip()
    result = get_outbreak_map_data(disease_filter=disease_filter)
    return jsonify(result)


@app.route("/api/outbreak-report", methods=["POST"])
def report_outbreak():
    data = request.get_json(silent=True) or {}
    district = data.get("district", "Dinajpur").strip()
    disease = data.get("disease", "").strip()
    result = record_outbreak_case(district, disease)
    return jsonify(result)


@app.route("/api/health", methods=["GET"])
@app.route("/healthz", methods=["GET"])
def healthcheck():
    return jsonify({
        "status": "healthy",
        "service": "RiceGuard AI",
        "model_loaded": True,
        "classes": 8,
        "threads": _torch_threads
    }), 200


@app.route("/manifest.json", methods=["GET"])
def serve_manifest():
    return send_from_directory(os.path.join(BASE_DIR, "static"), "manifest.json", mimetype="application/manifest+json")


@app.route("/sw.js", methods=["GET"])
def serve_service_worker():
    response = send_from_directory(os.path.join(BASE_DIR, "static"), "sw.js", mimetype="application/javascript")
    response.headers["Service-Worker-Allowed"] = "/"
    response.headers["Cache-Control"] = "no-cache"
    return response


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    print("Starting RiceGuard AI — Rice Leaf Disease Detection App...")
    print("Model: fair_augmented_cnn.pth (ResNet18)")
    print("Classes: 8")
    app.run(host="0.0.0.0", port=port, debug=False)
