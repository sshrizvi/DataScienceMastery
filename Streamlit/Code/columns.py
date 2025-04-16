import streamlit as st
import numpy as np

col1, col2 = st.columns(
    spec = [3, 1], 
    vertical_alignment = "bottom",
    gap = "medium"
)
data = np.random.randn(10, 1)

col1.markdown("#### Chart")
col1.line_chart(data)

col2.markdown("#### Values")
col2.write(data)