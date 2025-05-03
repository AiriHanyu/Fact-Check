import streamlit as st
from util import set_background_color

set_background_color("#12B9C8")

st.markdown('<h1 style="color:black; font-size: 100px; text-align: center;">ABOUT US</h1>', unsafe_allow_html=True)

st.markdown("""
    <div style="color: black;">
        <br><br>
        <h3>AIMAR ANSHARI</h3>
        <a href="https://instagram.com/aynshz_ryuxzy" style="color:black;">Instagram</a>
        <hr>
        <h3>MUTHMAINNAH NUR IZZAH</h3>
        <a href="https://instagram.com/innzzh" style="color:black;">Instagram</a>
    </div>
""", unsafe_allow_html=True)
