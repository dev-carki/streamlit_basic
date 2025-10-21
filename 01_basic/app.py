import streamlit as st

# modules
import config as cf
import text.text as texts
import number.number as numbers
import dataframe.dataframe as dataframes
import write_stream.write_stream as write_streams
import text_element.text_element as text_elements

# 단순 텍스트 작성
cf.set_title('단순 텍스트', 1)
texts.show()

# 정수 표시
cf.set_title('정수 표현', 2)
numbers.show()

# 데이터 프레임
cf.set_title('데이터 프레임', 3)
dataframes.show()

# 쓰기 스트림
cf.set_title('쓰기 스트림 - Chat GPT 처럼', 4)
write_streams.show()

cf.set_title('다양한 텍스트 요소들', 5)
text_elements.show()