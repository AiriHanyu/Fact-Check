import base64
import streamlit as st
import requests
from bs4 import BeautifulSoup
from docx import Document
import imageio_ffmpeg
import moviepy.config as mpconf
mpconf.change_settings({"FFMPEG_BINARY": imageio_ffmpeg.get_ffmpeg_exe()})
from moviepy.editor import VideoFileClip
import whisper
import os

def set_background_color(hex_color="#F0F0F0"):
    style = f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-color: {hex_color};
        }}
        </style>
    """
    st.markdown(style, unsafe_allow_html=True)

def render_text_output(text):
    st.markdown(f"""
        <div style="border: 1px solid #ccc; padding: 10px; border-radius: 5px;
                    background-color: #ffffff; color: black;
                    max-width: 100%; overflow-wrap: break-word;
                    word-wrap: break-word; text-align: justify;">
            {text.replace('\n','<br>')}
        </div>
    """, unsafe_allow_html=True)

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

def transcribe_video_to_text(video_file):
    """Ekstrak audio dari video dan langsung transkrip jadi teks"""
    temp_video_path = "temp_video.mp4"
    temp_audio_path = "temp_audio.mp3"
    with open(temp_video_path, "wb") as f:
        f.write(video_file.getbuffer())
    clip = VideoFileClip(temp_video_path)
    clip.audio.write_audiofile(temp_audio_path)
    result = model.transcribe(temp_audio_path)
    try:
        os.remove(temp_video_path)
        os.remove(temp_audio_path)
    except:
        pass
    return result["text"]

model = whisper.load_model("base")
def transcribe_audio(audio_file, temp_path="temp_audio.mp3"):
    """Transkrip file audio ke teks"""
    with open(temp_path, "wb") as f:
        f.write(audio_file.read())
    result = model.transcribe(temp_path)
    try:
        os.remove(temp_path)
    except FileNotFoundError:
        pass
    return result["text"]

def preprocess(text):
    # Lowercasing
    
    # Hapus angka dan karakter non-alphabet

    # Tokenisasi (bisa pakai spacy atau nltk)

    # Hapus stopwords
    
    return ' '.join("preprocessed")
