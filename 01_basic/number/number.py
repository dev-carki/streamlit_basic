import streamlit as st

def show():
    st.write('1 + 1 = ', 2)

    a = 1
    b = 2
    c = a + b
    st.write(f'{a} + {b} = ', c)