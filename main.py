import pandas as pd
import streamlit as st

#x = st.slider('YYY')
#st.write(x, 'sqr', x**2)
#st.write(x, 'sqr3', x**3)

st.header('Введение в проект')

st.subheader('Изучим файл train.csv')
train = pd.read_csv('train.csv')
st.write('Информация о датасете Train')
st.write(train.info())
st.write('Первые 10 строк датасета Train')
st.write(train.head(10))

#input
st.header('Введите данные')
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