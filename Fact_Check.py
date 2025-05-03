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

import streamlit as st

# Atur tombol dalam 3 kolom kecil yang nempel
col1, col2, col3 = st.columns([1, 1, 1])

# Simpan state aktif di session_state
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "TEXT"

# Bikin tombol & update state
with col1:
    if st.button("TEXT"):
        st.session_state.active_tab = "TEXT"
with col2:
    if st.button("URL"):
        st.session_state.active_tab = "URL"
with col3:
    if st.button("DOC"):
        st.session_state.active_tab = "DOC"

# Tampilkan input berdasarkan tab aktif
if st.session_state.active_tab == "TEXT":
    st.text_area("Masukkan teks di sini:", height=300)
elif st.session_state.active_tab == "URL":
    st.text_input("Tempelkan link berita di sini:")
elif st.session_state.active_tab == "DOC":
    uploaded_file = st.file_uploader("Upload file .docx, .txt, atau .pdf kamu di sini:", type=["docx", "txt", "pdf"])

