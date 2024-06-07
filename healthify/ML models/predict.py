import numpy as np
import tensorflow as tf
import cv2

# Load the trained model
model = tf.keras.models.load_model('skin_disease_model.h5')

def predict_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Could not read the image: {image_path}")
    img = cv2.resize(img, (128, 128))
    img = np.expand_dims(img, axis=0) / 255.0
    prediction = model.predict(img)
    predicted_class = np.argmax(prediction)
    return predicted_class, prediction

# Example usage
image_path = r'C:\Users\shake\OneDrive\Desktop\ML 24\data\testing\Acne\07AcnePittedScars1.jpg'  # Update this with the path to your test image
try:
    predicted_class, prediction = predict_image(image_path)
    print('Predicted Class:', predicted_class)
    print('Prediction Probabilities:', prediction)
except ValueError as e:
    print(e)
