import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# modules
import config as cf

def __say_hello():
    st.session_state["msg"] = "hello"
    return

def show():
    cf.desc("간단한 버튼", 1, 1)
    button_1 = st.button('버튼1')
    st.write(f"버튼 상태: {button_1}")
    
    if button_1:
        st.write("버튼이 눌렸습니다")
    
    button_click = st.button("버튼2 - hello", on_click=__say_hello)
    if "msg" in st.session_state:
        st.write(st.session_state["msg"])
        
    cf.desc("다운로드 버튼", 1, 2)
    df_csv = pd.DataFrame().to_csv()
    st.download_button(
        label='다운로드',
        data=df_csv,
        file_name='data.csv'
    )
    
    cf.desc('업로드 버튼', 1, 3)
    upload_files = st.file_uploader(
        'choose a csv file'
    )
    if upload_files:
        bytes_data = upload_files.read()
        st.write(dir(upload_files))
        st.write('file name> ', upload_files.name)
        st.write(bytes_data)
        
    cf.desc('카메라 버튼', 1, 4)
    picture = st.camera_input('카메라')
    if picture:
        st.image(picture)
        img = Image.open(picture)
        img_array = np.array(img)
        st.write(type(img_array))
        st.write(img_array.shape)
        
        img.save('./save.jpg')
    