import base64
import streamlit as st
import requests
from bs4 import BeautifulSoup

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
        # Mengambil konten dari URL
        response = requests.get(url)
        response.raise_for_status()  # Untuk memastikan bahwa request berhasil
        
        # Menggunakan BeautifulSoup untuk parse HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Mengambil semua teks dalam tag <p>
        paragraphs = soup.find_all('p')
        text = "\n".join([para.get_text() for para in paragraphs])
        
        return text
    except requests.exceptions.RequestException:
        # Jika ada masalah dengan request (misalnya URL tidak bisa diakses)
        return "Link tidak dapat diakses. Pastikan URL valid dan dapat dijangkau."
    except Exception:
        # Untuk kesalahan lainnya
        return "Akses ke URL ditolak atau kesalahan lainnya."
