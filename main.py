import streamlit as st
x = st.slider('YYY')
st.write(x, 'sqr', x**2)
st.write(x, 'sqr3', x**3)


ap_hi = st.slider('Систолическое (верхнее) давление', 80, 150 )
ap_lo = st.slider('Диастолическое (нижнее) давление', 40, 100 )

st.checkbox("Курите?", key="smoke")
