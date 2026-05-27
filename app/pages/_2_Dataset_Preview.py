import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("📚 Dataset Preview")

# LOAD DATA

data = pd.read_csv("../data/merged_data.csv")

st.subheader("🗂 Complete Dataset")

st.dataframe(
    data,
    use_container_width=True,
    height=700
)

st.subheader("📌 Dataset Information")

col1, col2 = st.columns(2)

col1.metric(
    "Rows",
    data.shape[0]
)

col2.metric(
    "Columns",
    data.shape[1]
)
