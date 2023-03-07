from typing import Any

import pandas as pd
import streamlit as st
import io
import pickle
import numpy as np
from sklearn.preprocessing import RobustScaler

# настраиваем вид страницы streamlit
st.set_page_config(page_title='Sergey Kuznetsov, Ya Practicum project for Kaggle competition',
                   layout='wide',
                   initial_sidebar_state='expanded')

st.title('Введение в проект', anchor='intro')
st.sidebar.header('[Введение в проект](#intro)')

# input
st.header('Проверим ваше сердце', anchor='heart')
st.sidebar.header('[Проверим ваше сердце](#heart)')
st.subheader(
    'Заполните информацию о своём здоровье на данный момент, чтобы узнать, какой есть риск сердечных заболеваний.')
lc, rc = st.columns(2)
age = lc.slider('Возраст', 20, 100, 35)
gender = rc.radio("Пол", options=("Мужчина", "Женщина"), key='gender')
height = lc.slider('Рост (см)', 150, 210, 175)
weight = rc.slider('Вес (кг)', 47, 150, 75)
ap_hi = lc.slider('Систолическое (верхнее) давление', 80, 150, 120)
ap_lo = rc.slider('Диастолическое (нижнее) давление', 40, 100, 70)

smoke = lc.radio("Курите?", options=("Нет", "Да"), key='smoke', horizontal=True)
alco = lc.radio("Пьёте?", options=("Нет", "Да"), key='alco', horizontal=True)

cholesterol = rc.selectbox("Уровень холестерина", ['Низкий', 'Средний', 'Высокий'], key="cholesterol", index=1)
gluc = rc.selectbox("Уровень глюкозы в крови", ['Низкий', 'Средний', 'Высокий'], key="gluc", index=1)
active = rc.selectbox("Уровень физической активности", ['Низкий', 'Высокий'], key="active")

st.write('')

# обработка
fl_ap = 0  # флажок, вверно ли введены данные
if ap_hi == ap_lo:
    st.warning('Верхнее давление не может быть равно нижнему')
elif ap_hi < ap_lo:
    st.warning('Верхнее давление не может быть выше нижнего. Проверьте данные!')
else:
    fl_ap = 1

imt = round(weight / ((height / 100) ** 2),2)
st.write('Жопа', str(imt))

""" if (fl_ap == 1) and (fl_imt == 1):
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


    #XGBoost не хочет подключаться к стримлиту, поэтому сделаем с RFC, он тоже неплох
    def load():
        with open('model_RFC.pcl', 'rb') as mod:
            return pickle.load(mod)
    model_test = load()

    age = age*365
    height = 168
    weight = 110
    ap_hi = 150
    ap_lo = 90
    gender = 1
    cholesterol = 1
    gluc = 1
    smoke = 1
    alco = 1
    active = 0

    #data = [[age,height,weight,ap_hi,ap_lo,gender,cholesterol,gluc,smoke,alco,active ]]

    data = pd.DataFrame({'age': age,
                  'height': height,
                  'weight': weight,
                  'ap_hi': ap_hi,
                  'ap_lo': ap_lo,
                  'gender_0': gender,
                  'gender_1': 0,
                  'cholesterol_0': cholesterol,
                  'cholesterol_1': 0,
                  'cholesterol_2': 0,
                  'gluc_0': gluc,
                  'gluc_1': 0,
                  'gluc_2': 0,
                  'smoke_0': 0,
                  'smoke_1': smoke,
                  'alco_0': 0,
                  'alco_1': alco,
                  'active_0': active,
                  'active_1': 0
                  }, index=[0])
    st.write(data.head())

    numeric = ['age', 'ap_hi', 'ap_lo', 'height', 'weight']

    features = pd.read_csv('features.csv')

    scaler = RobustScaler()
    scaler.fit(features[numeric])
    data[numeric] = scaler.transform(data[numeric])




    pr = model_test.predict_proba(data)[:,1]


    st.write(pr)
    st.write('Вероятность риска развития сердечно-сосудистого заболевания составляет {}'.format(pr))"""
st.write('Другие проекты в [моём профиле на GitHub](https://github.com/Kuuuzya)')
