import base64
import streamlit as st
import requests
from bs4 import BeautifulSoup
from docx import Document
import re
import string
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import joblib


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

stop_factory = StopWordRemoverFactory()
stopwords = stop_factory.get_stop_words()
stem_factory = StemmerFactory()
stemmer = stem_factory.create_stemmer()
def preprocess(text):
    text = str(text).lower()  # lowercase
    text = re.sub(r'<.*?>', ' ', text)  # hapus tag HTML
    text = re.sub(r'https?://\S+|www\.\S+', ' ', text)  # hapus URL
    text = re.sub(r'#\w+', ' ', text)  # hapus hashtag
    text = re.sub(r'\d+', ' ', text)  # hapus angka
    text = text.translate(str.maketrans('', '', string.punctuation))  # hapus tanda baca
    text = re.sub(r'\s+', ' ', text)  # hilangkan spasi ganda
    text = text.strip()  # hapus spasi awal/akhir
    text = re.sub(r'@\w+', '', text)  # hapus mention (@username)
    text = re.sub(r'[^\x00-\x7F]+', ' ', text) # hapus Emotikon
    # Token, Stopword Removal, dan Stemming
    tokens = text.split()
    tokens = [word for word in tokens if word not in stopwords]
    text = ' '.join(tokens)
    text = stemmer.stem(text)
    return text

model = joblib.load('model.pkl')
tfidf = joblib.load('tfidf.pkl')
with open("labels.txt", "r") as f:
    class_names = [line.strip().split('=')[1].strip() for line in f]

def classify(text):
    clean_text = preprocess(text)
    weight = tfidf.transform([clean_text])
    proba = model.predict_proba(weight)[0]
    label = model.predict(weight)[0]
    confidence = proba[label] * 100
    label_name = class_names[label]
    return label_name, confidence
