import streamlit as st

def set_title(text, index):
    st.markdown(f'# {index:02}. {text}')
    st.divider()
    
def __color_divider(color='darkblue'):
    st.markdown(
        f"""
        <hr style="border: 1px solid {color}; border-radius: 1px;">
        """,
        unsafe_allow_html=True
    )
    
def desc(label, index):
    __color_divider()
    st.markdown(f'## 5 - {index}. {label}')