import streamlit as st
import pandas as pd

uploaded_files = st.file_uploader(
    "Choose a CSV file", accept_multiple_files=True
)
for uploaded_file in uploaded_files:
    df = pd.read_csv(uploaded_file)
    st.write("File Name : ", uploaded_file.name)
    st.dataframe(df)