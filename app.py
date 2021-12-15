import streamlit as st
import pandas as pd
import numpy as np
import os
import pickle
from eda import run_eda_app as rea

def main():
    st.title('자동차 가격 예측')


    # 사이드바 메뉴
    menu = ['Home','EDA','ML']
    choice = st.sidebar.selectbox('메뉴',menu)

    if choice == 'Home':
        st.write('이 앱은 고객정보를 기반으로 한 차량 가격 예측 앱입니다. 고객의 데이터를 입력하면, 얼마정도의 차량을 구매할수 있는지 예측할 수 있습니다.')
        st.write('왼쪽의 사이드바에서 선택하세요.')
    elif choice == 'EDA':
        rea()
if __name__ == '__main__':
    main()