import streamlit as st
from util import set_background_color

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
import requests
from bs4 import BeautifulSoup

# Fungsi untuk ambil teks dari URL
def get_text_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            # Ambil semua teks dari halaman, filter yang cuma di dalam tag <p> (biasanya teks artikel)
            paragraphs = soup.find_all("p")
            article_text = "\n".join([para.get_text() for para in paragraphs])
            return article_text
        elif response.status_code == 403:
            return "Akses ditolak: Halaman memerlukan autentikasi atau blokir akses otomatis."
        elif response.status_code == 404:
            return "Halaman tidak ditemukan. Pastikan URL yang dimasukkan benar."
        else:
            return f"Terjadi kesalahan, status code: {response.status_code}. Coba periksa kembali link-nya."
    except requests.exceptions.RequestException as e:
        return f"Terjadi kesalahan saat mengakses link: {e}"

# Set CSS untuk mengatur warna teks dan centering
st.markdown("""
    <style>
        .stRadio > div {
            text-align: center;
            color: black;
        }
        .stTextArea, .stTextInput, .stFileUploader {
            display: block;
            margin: 0 auto;
            text-align: center;
            color: black;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; color: black;'>Pilih jenis input yang ingin kamu cek:</h3>", unsafe_allow_html=True)

option = st.radio("", ["TEXT", "URL", "DOCX"], horizontal=True)

col1, col2, col3 = st.columns(3)

if option == "TEXT":
    with col1:
        user_text = st.text_area("Masukkan teks di sini:")
elif option == "URL":
    with col2:
        user_url = st.text_input("Tempelkan link berita di sini:")
        if user_url:
            article_text = get_text_from_url(user_url)
            st.text_area("Teks dari artikel:", article_text, height=200)
elif option == "DOCX":
    with col3:
        uploaded_file = st.file_uploader("Upload file .docx kamu di sini:", type=["docx"])

# Tombol untuk cek fakta
if st.button("Cek Fakta"):
    st.write("Fungsi pengecekan fakta dijalankan di sini 🔍")
