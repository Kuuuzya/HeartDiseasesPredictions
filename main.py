import pandas as pd
import streamlit as st
import io
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder, RobustScaler
from sklearn.compose import ColumnTransformer

# настраиваем вид страницы streamlit
st.set_page_config(page_title='Sergey Kuznetsov, Ya Practicum project for Kaggle competition',
                   layout='wide',
                   initial_sidebar_state='expanded'
                   )
st.title('Проверим ваше сердце')
# input
#st.snow() #добавим снег, просто потому что почему бы и нет?!
st.markdown("<span style='color:lightgrey'>Заполните информацию о своём здоровье на данный момент, чтобы узнать, какой есть риск сердечных заболеваний.</span>", unsafe_allow_html=True)
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

# обработка
fl_ap = 0  # флажок, вверно ли введены данные
if ap_hi == ap_lo:
    st.sidebar.warning('Верхнее давление не может быть равно нижнему')
elif ap_hi < ap_lo:
    st.sidebar.warning('Верхнее давление не может быть выше нижнего. Проверьте данные!')
else:
    fl_ap = 1

imt = round(weight / ((height / 100) ** 2), 2)
fl_imt = 0
if height == weight:
    st.sidebar.warning('Вес равен росту. Так не бывает. Проверьте данные!', icon='⚠️')
    fl_imt = 0
elif imt < 16:
    st.sidebar.warning('Ваш ИМТ: ' + str(imt) + ', выраженный дефицит массы тела', icon='⚠️')
    fl_imt = 1
elif (imt >= 16) and (imt < 18.5):
    st.sidebar.warning('Ваш ИМТ: ' + str(imt) + ', недостаточная (дефицит) масса тела', icon='⚠️')
    fl_imt = 1
elif (imt >= 18.5) and (imt <= 25):
    st.sidebar.warning('Ваш ИМТ: ' + str(imt) + ', норма', icon='👍')
    fl_imt = 1
elif (imt > 25) and (imt <= 30):
    st.sidebar.warning('Ваш ИМТ: ' + str(imt) + ', избыточная масса тела (предожирение)', icon='⚠️')
    fl_imt = 1
elif (imt > 30) and (imt <= 35):
    st.sidebar.warning('Ваш ИМТ: ' + str(imt) + ', ожирение первой степени', icon='⚠️')
    fl_imt = 1
elif (imt > 35) and (imt <= 40):
    st.sidebar.warning('Ваш ИМТ: ' + str(imt) + ', ожирение второй степени', icon='⚠️')
    fl_imt = 1
elif (imt > 40) and (imt <= 60):
    st.sidebar.warning('Ваш ИМТ: ' + str(imt) + ', ожирение третьей степени', icon='⚠️')
    fl_imt = 1
else:
    st.sidebar.warning('Ваш ИМТ: ' + str(imt) + ', так не бывает. Проверьте данные!', icon='⚠️')
    fl_imt = 0

if (fl_ap == 1) and (fl_imt == 1):
    #XGBoost не хочет подключаться к стримлиту, поэтому сделаем с RFC, он тоже неплох
    def load():
        with open('model_XGB.pcl', 'rb') as mod:
            return pickle.load(mod)
    model_test = load()





    #подготовка данных для модели
    age = age*365.25
    if gender == "Женщина":
        gender=0
    else:
        gender = 1

    if smoke == "Да":
        smoke = 1
    else:
        smoke = 0

    if alco == "Да":
        alco = 1
    else:
        alco = 0

    if cholesterol == "Низкий":
        cholesterol = 0
    elif cholesterol == "Средний":
        cholesterol = 1
    else:
        cholesterol = 2

    if gluc == "Низкий":
        gluc = 0
    elif gluc == "Средний":
        gluc = 1
    else:
        gluc = 2

    if active == 'Низкий':
        active = 0
    else:
        active = 1


    #data = [[age,height,weight,ap_hi,ap_lo,gender,cholesterol,gluc,smoke,alco,active ]]

    data = pd.DataFrame({'age': age,
                  'height': height,
                  'weight': weight,
                  'ap_hi': ap_hi,
                  'ap_lo': ap_lo,
                  'gender': gender,
                  'cholesterol': cholesterol,
                  'gluc': gluc,
                  'smoke': smoke,
                  'alco': alco,
                  'active': active
                  }, index=[0])
    #st.write(data.head())
 #   numeric = ['age', 'ap_hi', 'ap_lo', 'height', 'weight']

#    features = pd.read_csv('features.csv')

 #   scaler = RobustScaler()
 #   scaler.fit(features[numeric])
 #   data[numeric] = scaler.transform(data[numeric])

    with open("pipe.pcl", "rb") as f:
        loaded_pipe = pickle.load(f)

    new_data_transformed = loaded_pipe.transform(data)
    numeric = ['age', 'ap_hi', 'ap_lo', 'height', 'weight']
    categorical = ['gender', 'cholesterol', 'gluc', 'smoke', 'alco', 'active']

    column_names = numeric + list(loaded_pipe.named_steps['preprocessor'].named_transformers_["cat"].get_feature_names_out(categorical))
    new_data_transformed_df = pd.DataFrame(new_data_transformed, columns=column_names)

    #st.write(new_data_transformed_df)
    pr = model_test.predict_proba(new_data_transformed_df)[:,1]

    st.sidebar.header('Результаты')
    pr = round(float(pr*100),2)
    if pr >= 50:
        st.sidebar.warning('Вероятность риска развития сердечно-сосудистого заболевания составляет: '+str(pr)+'%', icon='💔')
        if imt>25:
            st.sidebar.warning('Обратите внимание на ваш вес и индекс массы тела!')
        if (ap_hi > 150) or (ap_hi < 100):
            st.sidebar.warning('Обратите внимание на ваше верхнее давление!')
        if (ap_lo > 90) or (ap_lo < 50):
            st.sidebar.warning('Обратите внимание на ваше нижнее давление!')
        if (cholesterol == 1) or (cholesterol == 2):
            st.sidebar.warning('Обратите внимание на ваш уровень холестерина в крови!')
    else:
        st.sidebar.write('Риск развития сердечно-сосудистого заболевания составляет: ' + str(pr)+'%')
else:
    st.warning('Тут будут результаты, когда вы правильно введёте данные.')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write("_Другие проекты в [моём профиле на GitHub](https://github.com/Kuuuzya)_")


