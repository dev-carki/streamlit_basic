import streamlit as st
from datetime import datetime

def desc(label, start, index):
    st.markdown(f'### {start} - {index}. {label}')

def show():
    desc("다중선택", 3, 1)
    options_multiselect = st.multiselect(
        '다중선택 - 기본',
        ['1', '2', '3', '4'],
        default=['1']
    )
    st.write(options_multiselect)
    
    desc("pills", 3, 2)
    options_pills = ['1', '2', '3', '4']
    selection_basic = st.pills('pills - 기본', options=options_pills)
    st.write("선택된 항목: ", selection_basic)
    selection_multi = st.pills('pills - 다중선택 모드', options=options_pills, selection_mode='multi')
    st.write("선택된 항목: ", selection_multi)
    
    
    desc("선택 박스", 3, 3)
    options = st.selectbox('박스', ['1', '2', '3', '4'])
    st.write("선택된 항목: ", options)
    
    desc('슬라이더', 3, 4)
    st.slider(
        label='시작날짜',
        value=datetime(2025,10,22,15,10),
        format='YY/MM/DD hh:mm'
    )
    cat = st.slider(
        label='가로 위치',
        value=500,
        max_value=1000,
        step=50
    )

    st.write(cat)