import streamlit as st
from util import set_background_color

set_background_color("#12B9C8")

st.markdown('<h1 style="color:black; font-size: 100px; text-align: center; margin-bottom: 0;">FACT CHECK</h1>', unsafe_allow_html=True)
st.markdown(
    "<h4 style='text-align: center; color: black; font-family: \"Times New Roman\", serif;'>Not sure what to believe? Drop it here and let's check the facts and verify it here!</h4>",
    unsafe_allow_html=True
)



