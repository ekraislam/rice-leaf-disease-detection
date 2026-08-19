import os
import traceback
from flask import Flask, render_template, request, jsonify, send_from_directory, Response
import torch
from torchvision import transforms
from PIL import Image, UnidentifiedImageError
from src.model import get_baseline_cnn
from src.disease_data import DISEASE_DATABASE
from src.gradcam import GradCAM

# Optimize PyTorch CPU inference on shared cloud environments (prevents OOM / thread lockup)
torch.set_num_threads(1)

app = Flask(__name__)

# Enforce 10 MB maximum upload file size limit
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024
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
    state_dict = torch.load(MODEL_PATH, map_location=device)
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


from src.gradcam import GradCAM


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
                    image_tensor = transform(image).unsqueeze(0).to(device)

                    # Compute predictions
                    with torch.no_grad():
                        outputs = model(image_tensor)
                        probabilities = torch.softmax(outputs, dim=1)[0]
                        confidence_val, predicted_idx = torch.max(probabilities, dim=0)

                        # Compute Top-3 predictions
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

                    # Compute Grad-CAM Explainable AI Heatmap
                    try:
                        gcam = GradCAM(model)
                        cam_input = image_tensor.clone().detach().requires_grad_(True)
                        cam_map = gcam.generate(cam_input, class_idx=predicted_idx.item())
                        if cam_map is not None:
                            gradcam_url = gcam.overlay_heatmap(image, cam_map, alpha=0.5)
                        gcam.close()
                    except Exception as gcam_err:
                        print("Grad-CAM generation warning:", gcam_err)

                except UnidentifiedImageError:
                    error = "We couldn't read this image file. Please upload a valid image (JPG, PNG, BMP, or TIFF)."
                except Exception as e:
                    error = f"Analysis failed: {str(e)}"

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
        gradcam_url=gradcam_url,
        expected_class=expected_class,
        error=error,
        CLASS_NAMES=CLASS_NAMES,
        EXPECTED_CLASSES=EXPECTED_CLASSES,
        DISEASE_DATABASE=DISEASE_DATABASE
    )



import urllib.parse
import urllib.request
from flask import Response


@app.route("/api/tts", methods=["GET"])
def text_to_speech():
    disease = request.args.get("disease", "").strip()
    text = request.args.get("text", "").strip()
    lang = request.args.get("lang", "bn").strip()

    # Normalize disease slug
    if disease:
        slug = disease.lower().replace(" ", "_")
        audio_filename = f"{slug}_{lang}.mp3"
        audio_path = os.path.join(BASE_DIR, "static", "audio", audio_filename)
        if os.path.exists(audio_path):
            with open(audio_path, "rb") as f:
                return Response(f.read(), mimetype="audio/mpeg")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    try:
        # Split text into chunks <= 80 characters for Google TTS tw-ob API
        words = text.split(" ")
        chunks = []
        curr = ""
        for w in words:
            if len(curr) + len(w) + 1 <= 80:
                curr += (" " + w if curr else w)
            else:
                if curr:
                    chunks.append(curr)
                curr = w
        if curr:
            chunks.append(curr)

        combined = b""
        for c in chunks:
            encoded = urllib.parse.quote(c.strip())
            tts_url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={encoded}&tl={lang}&client=tw-ob"
            req = urllib.request.Request(
                tts_url,
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                }
            )
            with urllib.request.urlopen(req, timeout=6) as response:
                combined += response.read()

        return Response(combined, mimetype="audio/mpeg")
    except Exception as e:
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

