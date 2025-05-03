import base64
import streamlit as st

def set_background(image_file):
    with open(image_file, "rb") as f:
        img_data = f.read()
    b64_encoded = base64.b64encode(img_data).decode()
    style = f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64, {b64_encoded});
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }}
        </style>
    """
    st.markdown(style, unsafe_allow_html = True)
    
