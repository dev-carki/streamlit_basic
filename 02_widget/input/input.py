import streamlit as st

def __say_something(message):
    st.write(message)
    return

def show():
    text = st.text_input(
        '입력 텍스트',
        value="",
        max_chars=50,
        help="아무거나 입력하면 됩니다",
        placeholder="50자 이하의 텍스트를 입력하시오."
    )
    
    prompt = st.chat_input(placeholder="GPT에게 물어보시오")
    if prompt:
        __say_something(prompt)
    
    