import streamlit as st

# modules
import config as cf
import button.button as buttons
import checkbox.checkbox as checkboxes
import multi_select.multi_select as multi_selects
import input.input as inputs
    
cf.set_title("버튼", 1)
buttons.show()

cf.set_title('체크박스', 2)
checkboxes.show()

cf.set_title('다중 선택', 3)
multi_selects.show()

cf.set_title('입력', 4)
inputs.show()