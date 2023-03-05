import streamlit as st
#x = st.slider('YYY')
#st.write(x, 'sqr', x**2)
#st.write(x, 'sqr3', x**3)

#input
st.header('Введите данные')
ap_hi = st.slider('Систолическое (верхнее) давление', 80, 150 )
ap_lo = st.slider('Диастолическое (нижнее) давление', 40, 100 )

st.checkbox("Курю", key="smoke")

st.selectbox("Уровень холестерина",[0,1,2], key="cholesterol")

#output
st.header('Результаты')
st.write('Давление:', ap_hi,'/',ap_lo)
if st.session_state.smoke == False:
    st.write('Не курит')
else:
    st.write('Курит')
st.write('Уровень холестерина:', st.session_state.cholesterol)