import streamlit as st
import pandas as pd
from util import set_background_color

set_background_color("#A9A9A9")

st.markdown(
    '<h1 style="color:black; font-size: 50px; text-align: center;">RIWAYAT VERIFIKASI</h1>',
    unsafe_allow_html=True
)

# CSS custom biar tabel lebih besar
st.markdown("""
    <style>
    .big-font-table table {
        font-size:20px !important;     /* atur ukuran font isi tabel */
    }
    .big-font-table th {
        font-size:22px !important;     /* atur ukuran font header */
    }
    </style>
""", unsafe_allow_html=True)

# Data dummy
data = {
    "Waktu": ["09/09/2025 16:30", "09/09/2025 17:00", "09/09/2025 17:15"],
    "Narasi Berita": [
        "Berita A dicek dan masuk tahap validasi.",
        "Berita B terindikasi hoaks.",
        "Berita C sedang dalam proses klarifikasi."
    ],
    "Aksi": ["Silahkan menunggu konfirmasi selanjutnya"] * 3
}

df = pd.DataFrame(data)

# Tampilkan tabel dengan class custom
st.markdown('<div class="big-font-table">', unsafe_allow_html=True)
st.table(df)
st.markdown('</div>', unsafe_allow_html=True)
