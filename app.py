from flask import Flask, render_template, request, jsonify
import torch
from torchvision import transforms
from PIL import Image, UnidentifiedImageError
from src.model import get_baseline_cnn

app = Flask(__name__)

# Enforce 10 MB maximum upload file size limit
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

MODEL_PATH = "./models/fair_augmented_cnn.pth"

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
        expected_class=None,
        error=msg,
        CLASS_NAMES=CLASS_NAMES,
        EXPECTED_CLASSES=EXPECTED_CLASSES
    ), 413


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    confidence = None
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
                        probabilities = torch.softmax(outputs, dim=1)
                        confidence_value, predicted_class = torch.max(
                            probabilities, dim=1
                        )

                    prediction = CLASS_NAMES[predicted_class.item()]
                    confidence = round(
                        confidence_value.item() * 100, 2
                    )

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
                "expected_class": expected_class if expected_class else None,
                "error": None
            })

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        expected_class=expected_class,
        error=error,
        CLASS_NAMES=CLASS_NAMES,
        EXPECTED_CLASSES=EXPECTED_CLASSES
    )


if __name__ == "__main__":
    print("Starting RiceGuard AI — Rice Leaf Disease Detection App...")
    print("Model: fair_augmented_cnn.pth (ResNet18)")
    print("Classes: 8")
    app.run(host="127.0.0.1", port=5000, debug=False)

