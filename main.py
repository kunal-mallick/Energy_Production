import pickle
import math as mt
import numpy as np
import pandas as pd
import streamlit as st

load = open('model.pkl','rb')
model = pickle.load(load)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def main():
    for i in range(0,2):
        st.text('ok')

    col = st.columns(3)

    temp = col[0].number_input('Temperature', 1.81, 37.11)
    log_temp = mt.log(temp)

    ev = col[1].number_input('Exhaust Vacuum', 992.89, 1033.3)

    rh = col[2].number_input('Relative Humidity', 25.56, 100.16)
    log_rh = mt.log(rh)

    text = [[log_temp, ev, log_rh]]
    prediction = model.predict(text)

    col2 = st.columns(3)

    col2[0].image('https://raw.githubusercontent.com/kunal-mallick/Energy_Production/working/Images/Frame%202.png')
    col2[1].text('Energy -\n whould be    ' + '\n' +' ')
    col2[2].text('Production' + '\n' + str(round(prediction[0],2)) + ' MW')

if __name__ == '__main__':

    main()