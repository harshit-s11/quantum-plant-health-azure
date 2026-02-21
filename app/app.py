from flask import Flask, request, jsonify
from model_service import AzureModelService
import os

app = Flask(__name__)

model_service = AzureModelService()
model_service.load_model()

@app.route("/")
def home():
    return "Quantum Plant Health AI deployed on Azure 🚀"

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"})

    file = request.files["file"]
    file_path = "temp.jpg"
    file.save(file_path)

    prediction, confidence = model_service.predict(file_path)

    os.remove(file_path)

    return jsonify({
        "prediction": int(prediction),
        "confidence": confidence
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
