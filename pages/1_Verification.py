import streamlit as st
import pandas as pd
from util import set_background_color

set_background_color("#A9A9A9")

st.markdown(
    '<h1 style="color:black; font-size: 50px; text-align: center;">RIWAYAT VERIFIKASI</h1>',
    unsafe_allow_html=True
)

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

st.dataframe(df, use_container_width=True)
