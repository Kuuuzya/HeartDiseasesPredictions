import pandas as pd
import streamlit as st
import io
import pickle
import numpy as np
import sklearn
from sklearn.ensemble import RandomForestClassifier

#настраиваем вид страницы streamlit
st.set_page_config(page_title='Sergey Kuznetsov, Ya Practicum project for Kaggle competition',
                   layout='wide',
                   initial_sidebar_state='expanded')

st.title('Введение в проект', anchor='intro')
st.sidebar.header('[Введение в проект](#intro)')

#input
st.header('Проверим ваше сердце', anchor='heart')
st.sidebar.header('[Проверим ваше сердце](#heart)')
st.subheader('Заполните информацию о своём здоровье на данный момент, чтобы узнать, какой у вас риск сердечного приступа.')
lc, rc = st.columns(2)
ap_hi = lc.slider('Систолическое (верхнее) давление', 80, 150 )
ap_lo = rc.slider('Диастолическое (нижнее) давление', 40, 100 )

lc.checkbox("Курю", key="smoke")
rc.selectbox("Уровень холестерина",['Низкий', 'Средний', 'Высокий'], key="cholesterol")
rc.write('')
lc.write('')
st.write('')


#output
with lc:
    st.header('Результаты')
    st.write('Давление:', ap_hi,'/',ap_lo)
    if st.session_state.smoke == False:
        st.write('Не курит')
    else:
        st.write('Курит')

with rc:
    st.write('')
    st.write('')
    st.write('Уровень холестерина:', st.session_state.cholesterol.lower())


def load():
    with open('model_RFC.pcl', 'rb') as mod:
        return pickle.load(mod)
try:
    model_test = load()
    st.write('Модель загружена')
except:
    st.write('Модель НЕ загружена')

age = 35*365
height = 188
weight = 95
ap_hi = 120
ap_lo = 70
gender = 1
cholesterol = 1
gluc = 1
smoke = 1
alco = 1
active = 0

data = [[age,height,weight,ap_hi,ap_lo,gender,cholesterol,gluc,smoke,alco,active ]]
st.write(data)

pr = model_test.predict_proba(data)[:,1]

#st.write('Вероятность риска развития сердечно-сосудистого заболевания составляет {}'.format(y_pr))
st.write('Другие проекты в [моём профиле на GitHub](https://github.com/Kuuuzya)')