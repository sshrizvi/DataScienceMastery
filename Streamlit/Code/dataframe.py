import pandas as pd
import streamlit as st

df = pd.DataFrame(
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 28],
        'City': ['New York', 'London', 'Paris']
    }
)

st.dataframe(
    data = df
)