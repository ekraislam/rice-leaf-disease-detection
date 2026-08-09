from flask import Flask, render_template, request
import torch
from torchvision import transforms
from PIL import Image
from src.model import get_baseline_cnn

app = Flask(__name__)

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


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    confidence = None
    expected_class = None
    error = None

    if request.method == "POST":
        expected_class = request.form.get("expected_class", "").strip()
        if "image" not in request.files:
            error = "Please select an image."
        else:
            file = request.files["image"]

            if file.filename == "":
                error = "Please select an image."
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

                except Exception as e:
                    error = f"Prediction failed: {str(e)}"

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
    print("Starting Rice Leaf Disease Detection App...")
    print("Model: fair_augmented_cnn.pth")
    print("Classes: 8")
    app.run(host="127.0.0.1", port=5000, debug=False)
