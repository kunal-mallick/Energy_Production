import streamlit as st
import pandas as pd

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

x =  4400
for i in range(0,2):
    st.text('ok')

col = st.columns(3)

col[0].number_input('Temperature', 1.81, 37.11)
col[1].number_input('Exhaust Vacuum', 992.89, 1033.3)
col[2].number_input('Relative Humidity', 25.56, 100.16)

col2 = st.columns(3)

col2[0].image('https://raw.githubusercontent.com/kunal-mallick/Energy_Production/working/Images/Frame%202.png')
col2[1].text('Energy\n whould be    ' + '\n' +' ')
col2[2].text('Production' + '\n' + str(x) + ' MW')