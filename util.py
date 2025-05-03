import base64
import streamlit as st
import requests
from bs4 import BeautifulSoup
from docx import Document

def set_background_color(hex_color="#F0F0F0"):
    style = f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-color: {hex_color};
        }}
        </style>
    """
    st.markdown(style, unsafe_allow_html=True)

def get_text_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        text = "\n".join([para.get_text() for para in paragraphs])
        return text
    except requests.exceptions.RequestException:
        return "Link tidak dapat diakses. Pastikan URL valid dan dapat dijangkau."
    except Exception:
        return "Akses ke URL ditolak atau kesalahan lainnya."

def read_uploaded_file(file):
    """Fungsi untuk membaca isi teks dari file DOCX atau TXT yang di-upload."""
    if file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    elif file.name.endswith(".docx"):
        doc = Document(file)
        doc_text = ""
        for para in doc.paragraphs:
            doc_text += para.text + "\n"
        return doc_text
    else:
        return "Format file tidak didukung."
