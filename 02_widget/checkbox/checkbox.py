import streamlit as st

def show():
    agree = st.checkbox('동의')
    st.write('체크박스 상태: ', agree)