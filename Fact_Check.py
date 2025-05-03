import streamlit as st
from util import set_background_color
import requests
from bs4 import BeautifulSoup

set_background_color("#12B9C8")

st.markdown('<h1 style="color:black; font-size: 100px; text-align: center; margin-bottom: 0;">FACT CHECK</h1>', unsafe_allow_html=True)
st.markdown(
    """
    <head>
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">
    </head>
    <h4 style='text-align: center; color: black; margin-top: 0; font-family: "Roboto", sans-serif; font-weight: 300;'>
        Not sure what to believe? Drop it here and let's check the facts and verify it here!
    </h4>
    """,
    unsafe_allow_html=True
)

option = st.radio("", ["TEXT", "URL", "DOCX"], horizontal=True)

if option == "TEXT":
    st.text_area("Masukkan teks di sini:", height=300) 
elif option == "URL":
    st.text_input("Tempelkan link berita di sini:")  
elif option == "DOCX":
    uploaded_file = st.file_uploader("Upload file .docx kamu di sini:", type=["docx"]) 
