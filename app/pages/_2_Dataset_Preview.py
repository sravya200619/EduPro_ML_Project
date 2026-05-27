import streamlit as st
import pandas as pd
from pathlib import Path
st.set_page_config(layout="wide")

st.title("📚 Dataset Preview")

# LOAD DATA

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

data_path = BASE_DIR / "data" / "merged_data.csv"

data = pd.read_csv(data_path)

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
