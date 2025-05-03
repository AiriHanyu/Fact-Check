import streamlit as st
from util import set_background_color, get_text_from_url, read_uploaded_file

set_background_color("#12B9C8")

st.markdown('<h1 style="color:black; font-size: 100px; text-align: center; margin-bottom: 0;">FACT CHECK</h1>', unsafe_allow_html=True)
st.markdown(
    """
    <head>
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">
    </head>
    <h4 style='text-align: center; color: black; margin-top: 0; font-family: "Roboto", sans-serif; font-weight: 300;'>
        Not sure what to believe? Drop it here and let's check the facts and verify it here!
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

col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 2, 1])

with col2:
    if st.button("TEXT", use_container_width=True):
        st.session_state.tab = "TEXT"
with col3:
    if st.button("URL", use_container_width=True):
        st.session_state.tab = "URL"
with col4:
    if st.button("DOCX", use_container_width=True):
        st.session_state.tab = "DOC"

if st.session_state.tab:
    if st.session_state.tab == "TEXT":
        user_text = st.text_area("", height=300)
    elif st.session_state.tab == "URL":
        user_url = st.text_input("")
    elif st.session_state.tab == "DOC":
        uploaded_file = st.file_uploader("", type=["docx", "txt"])

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3, col4, col5 = st.columns([1, 2, 1, 2, 1])
    with col3:
        view = st.button("View")

    if view:
        with st.container():
            if st.session_state.tab == "TEXT" and user_text:
                st.markdown(f"""
                    <div style="border: 1px solid #ccc; padding: 10px; border-radius: 5px;
                                background-color: #ffffff; color: black;
                                max-width: 100%; overflow-wrap: break-word;
                                word-wrap: break-word;">
                        {user_text}
                    </div>
                """, unsafe_allow_html=True)
    
            elif st.session_state.tab == "URL" and user_url:
                article_text = get_text_from_url(user_url)
                st.markdown(f"""
                    <div style="border: 1px solid #ccc; padding: 10px; border-radius: 5px;
                                background-color: #ffffff; color: black;
                                max-width: 100%; overflow-wrap: break-word;
                                word-wrap: break-word;">
                        {article_text}
                    </div>
                """, unsafe_allow_html=True)
                
            elif st.session_state.tab == "DOC" and uploaded_file:
                doc_text = read_uploaded_file(uploaded_file)
                st.markdown(f"""
                    <div style="border: 1px solid #ccc; padding: 10px; border-radius: 5px;
                                background-color: #ffffff; color: black;
                                max-width: 100%; overflow-wrap: break-word;
                                word-wrap: break-word;">
                        {doc_text}
                    </div>
                """, unsafe_allow_html=True)
    


st.markdown(
    "<hr style='border: 1.5px solid black; margin: 20px 0;'>",
    unsafe_allow_html=True
)
