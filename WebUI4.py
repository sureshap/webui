

import streamlit as st
import numpy as np
import pandas as pd

uploaded_file = st.file_uploader("Choose a XLSX file", type="xlsx")

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    df_show = df.head(10)
    st.dataframe(df_show)
    st.table(df_show)
