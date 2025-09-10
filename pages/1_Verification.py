import streamlit as st
import pandas as pd
from util import set_background_color

set_background_color("#A9A9A9")

st.markdown(
    '<h1 style="color:black; font-size: 50px; text-align: center;">RIWAYAT VERIFIKASI</h1>',
    unsafe_allow_html=True
)

columns = ["Waktu", "Narasi Berita", "Prediksi", "Hasil Verifikasi", "Referensi", "Report"]

# Ambil dari session_state.history (yang diisi di page FACT CHECK)
history = st.session_state.get("history", [])

# Tombol reset/clear riwayat
c1, c2, c3 = st.columns([1,2,1])
with c2:
    if st.button("Hapus Semua Riwayat", use_container_width=True):
        st.session_state.history = []
        history = []

# Buat DataFrame dan tampilkan
df = pd.DataFrame(history, columns=columns)
st.dataframe(df, use_container_width=True)


