import streamlit as st
import pandas as pd
import numpy as np
import joblib
def run_ml_app():
    st.subheader('Machine Learning 예측')
    # 1. 유저한테 데이터를 입력 받습니다.
    gender = st.radio("성별을 입력하세요",['남자','여자'])
    if gender == '남자':
        gender_number = 1
    else:
        gender_number = 0
    age = st.number_input('나이를 입력 해주세요',min_value=1,max_value=120)
    salary = st.number_input('연봉 입력',min_value=10000)
    dept = st.number_input('카드 빚 입력',min_value=0)
    worth = st.number_input('자산 입력',min_value=10000)
    # 2. 모델에 예측한다.
    new_data = np.array([gender_number,age,salary,dept,worth])
    new_data = new_data.reshape(1,5)
    # 2-2 스케일러와 인공지능 불러오기
    scaler_X = joblib.load('data/scaler_X.pkl')
    scaler_y = joblib.load('data/scaler_y.pkl')
    regressor = joblib.load('data/regressor.pkl')
    # 2-3 신규 데이터를 피처스케일링 한다.
    new_data = scaler_X.transform(new_data)
    # 2-4 인공지능에게 예측을 하게 한다.
    y_pred = regressor.predict(new_data)
    # 2-5 예측한 결과는 다시 복구
    y_pred = y_pred.reshape(1,1)
    y_pred = scaler_y.inverse_transform(y_pred)
    # 3. 예측 결과를 웹 대시보드에 표시한다.
    btn = st.button('예측결과 보기')
    if btn:
        st.write(f'예측결과 {int(y_pred[0,0])}$ 의 차를 살수 있습니다.')