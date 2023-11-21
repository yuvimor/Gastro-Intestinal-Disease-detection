import streamlit as st
from keras.models import load_model
import gdown
import os
# Specify the display to use 
os.environ['DISPLAY'] = ':1' 
import cv2
import numpy as np

# Download the ResNet50 model from Google Drive
url = "https://drive.google.com/file/d/1dgFl1vvdp_j3mdkmTGshB4zZnEhpYPT-/view?usp=sharing"  
output = "resnet50_model.h5"
gdown.download(url, output, quiet=False)

# Load the downloaded ResNet50 model
model_resnet50 = load_model("resnet50_model.h5")

# Streamlit app code
st.title("Gastrointestinal Disease Detection App")

# Upload an image for prediction
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    # Read the uploaded image
    image = cv2.imread(uploaded_file.name)
    
    # Resize the image to match the input size used during training
    img_resize_rgb = cv2.resize(image, (100, 100))
    
    # Expand the dimensions to match the model input shape
    img_input = np.expand_dims(img_resize_rgb, axis=0)
    
    # Normalize pixel values to the range [0, 1]
    img_input = img_input / 255.0
    
    # Make predictions using the loaded model
    prediction = model_resnet50.predict(img_input)

    # Display the results
    st.image(img_resize_rgb[:, :, ::-1], caption="Uploaded Image.", use_column_width=True)
    st.write(f"Prediction: {categories[np.argmax(prediction)]}")
