import base64
import streamlit as st
from PIL import Image, ImageOps
import numpy as np

def classify(image, model, class_names):
    
    image = ImageOps.fit(image, (224, 224), method = Image.Resampling.LANCZOS)
    
    image_array = np.asarray(image)
    
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array
    
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]
    
    return class_name, confidence_score


    
