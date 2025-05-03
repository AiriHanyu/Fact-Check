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

col1, col2, col3 = st.columns([1, 1, 1])
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "TEXT"
with col1:
    if st.button("TEXT"):
        st.session_state.active_tab = "TEXT"
with col2:
    if st.button("URL"):
        st.session_state.active_tab = "URL"
with col3:
    if st.button("DOC"):
        st.session_state.active_tab = "DOC"

if option == "TEXT":
    st.text_area("Masukkan teks di sini:", height=300) 
elif option == "URL":
    st.text_input("Tempelkan link berita di sini:")  
elif option == "DOCX/TXT/PDF":
    uploaded_file = st.file_uploader("Upload file .docx, .txt kamu di sini:", type=["docx", "txt"])

