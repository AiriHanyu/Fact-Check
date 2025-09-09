import streamlit as st

set_background_color("#A9A9A9")

st.title("Riwayat Verifikasi")

if "results" not in st.session_state:
    st.session_state.results = []

if "last_result" in st.session_state:
    data = st.session_state.last_result
    proba = data["proba"]

    label = "HOAKS" if proba[0][0] > 0.5 else "VALID"
    st.session_state.results.append({
        "Waktu": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "Narasi Berita": data["text"],
        "Prediksi": label,
        "Silahkan Menunggu Konfirmasi Selanjutnya": ""
    })

    del st.session_state.last_result

if len(st.session_state.results) == 0:
    st.info("Belum ada data verifikasi.")
else:
    df = pd.DataFrame(st.session_state.results)
    st.table(df)
