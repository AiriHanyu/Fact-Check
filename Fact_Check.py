import streamlit as st
from util import set_background_color, get_text_from_url, read_uploaded_file, classify, circle_progress
import html

set_background_color("#A9A9A9")

labels = ["HOAKS", "VALID"]
colors = ["#FF4B4B", "#1AB13D"] 


st.markdown('<h1 style="color:black; font-size: 100px; text-align: center; margin-bottom: 0;">FACT CHECK</h1>', unsafe_allow_html=True)
st.markdown(
    """
    <head>
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">
    </head>
    <h4 style='text-align: center; color: black; font-family: "Roboto", sans-serif; font-weight: 300;'>
        Not sure what to believe? Let's check the facts and verify it here!
    </h4>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<hr style='border: 1.5px solid black; margin: 20px 0;'>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

if "tab" not in st.session_state:
    st.session_state.tab = None

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

if st.session_state.tab:
    if st.session_state.tab == "TEXT":
        user_text = st.text_area("", height=300)
    elif st.session_state.tab == "URL":
        user_url = st.text_input("")
    elif st.session_state.tab == "DOC":
        uploaded_file = st.file_uploader("", type=["docx", "txt"])
    elif st.session_state.tab == "MP3":
        st.markdown('<h1 style="color:black; font-size: 24px; text-align: center; margin-bottom: 0;">Masih dalam tahap pengembanganq</h1>', unsafe_allow_html=True)
    elif st.session_state.tab == "MP4":
        st.markdown('<h1 style="color:black; font-size: 24px; text-align: center; margin-bottom: 0;">Masih dalam tahap pengembanganq</h1>', unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns([1, 2, 1, 2, 1])
    with col3:
        view = st.button("Check")

    if view:
        with st.container():
            if st.session_state.tab == "TEXT" and user_text:
                proba = classify(user_text)[0]  # hasil probabilitas array
                st.markdown('<h1 style="color:black; font-size: 48px; text-align: center; margin-bottom: 0;">HASIL PREDIKSI</h1>', unsafe_allow_html=True)
                html_blocks = []  # reset blok setiap input baru
                for i in range(len(labels)):
                    percent = proba[i] * 100
                    html_blocks.append(circle_progress(labels[i], percent, colors[i]))
                st.markdown(
                    f"""
                    <div style="display: flex; justify-content: center;">
                        {' '.join(html_blocks)}
                    </div>
                    """, unsafe_allow_html=True
                )
                
            elif st.session_state.tab == "URL" and user_url:
                article_text = get_text_from_url(user_url)
                proba = classify(article_text)[0]  # hasil probabilitas array
                st.markdown('<h1 style="color:black; font-size: 48px; text-align: center; margin-bottom: 0;">HASIL PREDIKSI</h1>', unsafe_allow_html=True)
                html_blocks = []  # reset blok setiap input baru
                for i in range(len(labels)):
                    percent = proba[i] * 100
                    html_blocks.append(circle_progress(labels[i], percent, colors[i]))
                st.markdown(
                    f"""
                    <div style="display: flex; justify-content: center;">
                        {' '.join(html_blocks)}
                    </div>
                    """, unsafe_allow_html=True
                )
                
            elif st.session_state.tab == "DOC" and uploaded_file:
                doc_text = read_uploaded_file(uploaded_file)
                proba = classify(doc_text)[0]  # hasil probabilitas array
                st.markdown('<h1 style="color:black; font-size: 48px; text-align: center; margin-bottom: 0;">HASIL PREDIKSI</h1>', unsafe_allow_html=True)
                html_blocks = []  # reset blok setiap input baru
                for i in range(len(labels)):
                    percent = proba[i] * 100
                    html_blocks.append(circle_progress(labels[i], percent, colors[i]))
                st.markdown(
                    f"""
                    <div style="display: flex; justify-content: center;">
                        {' '.join(html_blocks)}
                    </div>
                    """, unsafe_allow_html=True
                )

            elif st.session_state.tab == "MP3" and uploaded_file:
                st.markdown('<h1 style="color:black; font-size: 24px; text-align: center; margin-bottom: 0;">Masih dalam tahap pengembanganq</h1>', unsafe_allow_html=True)
            
            elif st.session_state.tab == "MP4" and uploaded_file:
                st.markdown('<h1 style="color:black; font-size: 24px; text-align: center; margin-bottom: 0;">Masih dalam tahap pengembanganq</h1>', unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown(
                "<hr style='border: 1.5px solid black; margin: 20px 0;'>",
                unsafe_allow_html=True
            )

            st.markdown("<br>", unsafe_allow_html=True)
