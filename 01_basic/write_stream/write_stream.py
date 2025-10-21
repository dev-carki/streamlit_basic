import streamlit as st
import time

zep_info_text = "슈퍼캣과 네이버제트의 합작법인 'ZEP'이 운영하는 동명의 메타버스 플랫폼이다. 2021년 11월 30일 베타버전을 시작했으며 2022년 3월 16일 정식서비스를 시작했다. 쉽고 재미있는 메타버스라는 컨셉으로 출발하여 현재 부트캠프, 학교, HRD, 행사, 브랜딩, 오피스 용도로 널리 쓰이고 있으며, 현재는 학교에서 가장 많이 사용되고 있다."
def __stream_data():
    for word in zep_info_text.split(" "):
        yield word + " "
        time.sleep(0.1)

def show():
    if st.button('스트림 텍스트'):
        st.write_stream(__stream_data)