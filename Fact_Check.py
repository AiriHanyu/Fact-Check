import streamlit as st
from util import set_background_color

set_background_color("#12B9C8")

st.markdown("""
    <div style="text-align: center;">
        <h1 style="color:black; font-size: 100px; margin-bottom: 0px; line-height: 1.1;">FACT CHECK</h1>
        <h4 style="color: black; margin-top: 0px; line-height: 1;">Not sure what to believe? Drop it here and let's check the facts and verify it here!</h4>
    </div>
""", unsafe_allow_html=True)

