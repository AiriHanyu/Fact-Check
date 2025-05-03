import streamlit as st
from keras.models import load_model 
from PIL import ImageOps, Image
from util import classify

st.title(":green[AI Image Investigator] :mag_right:")

uploaded_files = st.file_uploader(
    "Upload Gambar",
    type=["jpg", "jpeg", "png", "webp"],
    accept_multiple_files=True
)

model = load_model('model_vgg16.h5')

with open('labels.txt', 'r') as f:
    class_names = [a[:-1].split(' ')[1] for a in f.readlines()]
    f.close()

if uploaded_files:
    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption=uploaded_file.name, use_container_width=True)
        
        class_name, conf_score = classify(image, model, class_names)
        
        st.write("## {}".format(class_name))
        st.write("### score: {}".format(conf_score))
