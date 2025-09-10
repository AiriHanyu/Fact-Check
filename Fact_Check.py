import streamlit as st
import numpy as np
from datetime import datetime
from util import set_background_color, get_text_from_url, read_uploaded_file, classify, circle_progress
from textwrap import dedent

set_background_color("#A9A9A9")

labels = ["HOAKS", "VALID"]
colors = ["#FF4B4B", "#1AB13D"]

# --- INIT SESSION STATE ---
if "tab" not in st.session_state:
    st.session_state.tab = None
if "history" not in st.session_state:
    st.session_state.history = []  # list of dict, akan dibaca di halaman Riwayat

st.markdown(
    """<h1 style="color:black; font-size: 100px; text-align: center; margin-bottom: 0;">FACT CHECK</h1>""",
    unsafe_allow_html=True
)
st.markdown(
    dedent("""
    <head>
      <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">
    </head>
    <h4 style='text-align: center; color: black; font-family: "Roboto", sans-serif; font-weight: 300;'>
      Not sure what to believe? Let's check the facts and verify it here!
    </h4>
    """),
    unsafe_allow_html=True
)
st.markdown("""<hr style='border: 1.5px solid black; margin: 20px 0;'>""", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 2, 2, 2, 2, 2, 1])
with col2:
    if st.button("TEXT", use_container_width=True):
        st.session_state.tab = "TEXT"
with col3:
    if st.button("URL", use_container_width=True):
        st.session_state.tab = "URL"
with col4:
    if st.button("DOC", use_container_width=True):
        st.session_state.tab = "DOC"
with col5:
    if st.button("MP3", use_container_width=True):
        st.session_state.tab = "MP3"
with col6:
    if st.button("MP4", use_container_width=True):
        st.session_state.tab = "MP4"

def render_prediction(proba):
    st.markdown("""<h1 style="color:black; font-size: 48px; text-align: center; margin-bottom: 0;">HASIL PREDIKSI</h1>""",
                unsafe_allow_html=True)
    html_blocks = []
    for i in range(len(labels)):
        percent = proba[i] * 100
        html_blocks.append(circle_progress(labels[i], percent, colors[i]))
    st.markdown(dedent(f"""
    <div style="display:flex;justify-content:center;gap:24px;flex-wrap:wrap;">
    {''.join(html_blocks)}
    </div>
    """), unsafe_allow_html=True)

view = False
user_text = user_url = None
uploaded_file = None

if st.session_state.tab:
    if st.session_state.tab == "TEXT":
        user_text = st.text_area("", height=300)
    elif st.session_state.tab == "URL":
        user_url = st.text_input("")
    elif st.session_state.tab == "DOC":
        uploaded_file = st.file_uploader("", type=["docx", "txt"])
    elif st.session_state.tab == "MP3":
        st.markdown("""<h1 style="color:black; font-size: 24px; text-align: center; margin-bottom: 0;">Masih dalam tahap pengembangan</h1>""",
                    unsafe_allow_html=True)
    elif st.session_state.tab == "MP4":
        st.markdown("""<h1 style="color:black; font-size: 24px; text-align: center; margin-bottom: 0;">Masih dalam tahap pengembangan</h1>""",
                    unsafe_allow_html=True)

    if st.session_state.tab not in ["MP3", "MP4"]:
        c1, c2, c3, c4, c5 = st.columns([1, 2, 1, 2, 1])
        with c3:
            view = st.button("Check", use_container_width=True)

    if view:
        with st.container():
            raw_text = None
            referensi = ""
            proba = None

            if st.session_state.tab == "TEXT" and user_text:
                raw_text = user_text
                proba = classify(user_text)[0]
                referensi = "-"

            elif st.session_state.tab == "URL" and user_url:
                article_text = get_text_from_url(user_url)
                raw_text = article_text
                proba = classify(article_text)[0]
                referensi = user_url

            elif st.session_state.tab == "DOC" and uploaded_file:
                doc_text = read_uploaded_file(uploaded_file)
                raw_text = doc_text
                proba = classify(doc_text)[0]
                referensi = getattr(uploaded_file, "name", "-")

            if proba is not None and raw_text:
                render_prediction(proba)

                # --- SIMPAN KE HISTORY UNTUK PAGE RIWAYAT ---
                top_idx   = int(np.argmax(proba))
                top_label = labels[top_idx]
                top_prob  = proba[top_idx] * 100
                # prediksi_str sekarang hanya 1 nilai (yang tertinggi)
                prediksi_str = f"{top_label}: {top_prob:.1f}%"
                st.session_state.history.append({
                    "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "Narasi Berita": ringkas_narasi,
                    "Prediksi": prediksi_str,
                    "Hasil Verifikasi": "",
                    "Referensi": referensi,
                    "Report": ""  
                })

            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("<hr style='border: 1.5px solid black; margin: 20px 0;'>", unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)


















