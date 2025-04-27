from tensorflow.keras.models import load_model
import joblib
import numpy as np
from PIL import Image
import cv2

# brain_tumor_model = load_model("models/brain_tumor_model.h5")
pneumonia_model = load_model("models/pneumonia_model.h5")
# diabetes_model = joblib.load("models/diabetes_model.pkl")
# heart_disease_model = joblib.load("models/heart_disease_model.pkl")


def predict_pneumonia(image_file):
    # Read the uploaded image file into a numpy array
    file_bytes = np.frombuffer(image_file.read(), np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Preprocess
    img = cv2.resize(img, (150, 150))
    img = img.reshape(1, 150, 150, 3)
    img = img / 255.0

    # Prediction
    pred = pneumonia_model.predict(img)
    return "Pneumonia" if pred > 0.5 else "Normal"