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

st.markdown(
    "<hr style='border: 1.5px solid black; margin: 20px 0;'>",
    unsafe_allow_html=True
)

if "tab" not in st.session_state:
    st.session_state.tab = "TEXT"

col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 2, 1])

with col2:
    if st.button("TEXT", use_container_width=True):
        st.session_state.tab = "TEXT"
with col3:
    if st.button("URL", use_container_width=True):
        st.session_state.tab = "URL"
with col4:
    if st.button("DOCX", use_container_width=True):
        st.session_state.tab = "DOCX"

if st.session_state.tab == "TEXT":
    st.text_area("Masukkan teks di sini:", height=300)
elif st.session_state.tab == "URL":
    st.text_input("Tempelkan link berita di sini:")
elif st.session_state.tab == "DOCX":
    st.file_uploader("Upload file .docx, .txt, atau .pdf kamu di sini:", type=["docx", "txt", "pdf"])
