import streamlit as st
import pandas as pd

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

a = st.container()
a.image("https://raw.githubusercontent.com/kunal-mallick/Energy_Production/main/Images/burullus-260917-dji-0026-2.jpg")
a.text('ok')