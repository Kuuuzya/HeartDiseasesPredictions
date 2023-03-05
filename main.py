import streamlit as st
x = st.slider('YYY')
st.write(x, 'sqr', x**2)
st.write(x, 'sqr3', x**3)


ap_hi = st.slider('Систолическое (верхнее) давление', 80, 150 )
ap_lo = st.slider('Диастолическое (нижнее) давление', 40, 100 )

st.checkbox("Курю", key="smoke")

st.selectbox("Уровень холестерина",[0,1,2], key="cholesterol")

st.write('Давление:', ap_hi,'/',ap_lo)
st.write('Курение:', smoke)
st.write('Уровень холестерина:', cholesterol)