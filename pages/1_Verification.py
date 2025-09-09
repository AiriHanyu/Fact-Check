import streamlit as st
import pandas as pd
from util import set_background_color

set_background_color("#A9A9A9")

st.markdown(
    '<h1 style="color:black; font-size: 50px; text-align: center;">RIWAYAT VERIFIKASI</h1>',
    unsafe_allow_html=True
)

# Bikin DataFrame kosong dengan kolom sesuai template
columns = ["Waktu", "Narasi Berita", "Prediksi", "Hasil Verifikasi", "Referensi", "Report"]
df = pd.DataFrame(columns=columns)

# Tampilkan tabel
st.dataframe(df, use_container_width=True)
