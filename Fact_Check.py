import streamlit as st
from util import set_background_color

set_background_color("12B9C8")
st.markdown('<h1 style="color:black; font-size: 100px; text-align: center; margin-bottom: 10px;">FACT CHECK</h1>', unsafe_allow_html=True)

st.markdown(
    "<h4 style='text-align: center; color: black; margin-top: 0;'>Not sure what to believe? Drop it here and let's check the facts and verify it here!</h4>",
    unsafe_allow_html=True
)


