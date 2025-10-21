import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

def show():
    simple_dataframe = pd.DataFrame(
        {
            'col1': [1, 2, 3 ,4],
            'col2': [10, 20, 30, 40],
        }
    )
    simple_table = st.write(simple_dataframe)

    simple_dataframe2 = pd.DataFrame(
        np.random.randn(200, 3),
        columns=['a', 'b', 'c']
    )
    st.write(simple_dataframe2)
    
    # 챠트
    chart = (
        alt
        .Chart(simple_dataframe2)
        .mark_circle()
        .encode(x="a", y="b", size="c", color="c", tooltip=["a","b","c"])
    )
    st.write(chart)