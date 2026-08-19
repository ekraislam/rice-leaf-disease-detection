import os
import traceback
from flask import Flask, render_template, request, jsonify
import torch
from torchvision import transforms
from PIL import Image, UnidentifiedImageError
from src.model import get_baseline_cnn
from src.disease_data import DISEASE_DATABASE

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


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    confidence = None
    top_predictions = None
    disease_info = None
    expected_class = None
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
                                "severity": c_info.get("severity", ""),
                                "severity_color": c_info.get("severity_color", "#10B981")
                            })

                    prediction = CLASS_NAMES[predicted_idx.item()]
                    confidence = round(confidence_val.item() * 100, 2)
                    disease_info = DISEASE_DATABASE.get(prediction, {})

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
        error=error,
        CLASS_NAMES=CLASS_NAMES,
        EXPECTED_CLASSES=EXPECTED_CLASSES,
        DISEASE_DATABASE=DISEASE_DATABASE
    )



if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    print("Starting RiceGuard AI — Rice Leaf Disease Detection App...")
    print("Model: fair_augmented_cnn.pth (ResNet18)")
    print("Classes: 8")
    app.run(host="0.0.0.0", port=port, debug=False)

