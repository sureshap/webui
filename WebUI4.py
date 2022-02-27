

import streamlit as st
import numpy as np
import pandas as pd


st.write('Hello')

# A function to load the data.
DATE_COLUMN = 'date/time'
DATA_URL = ('input_data.xlsx')

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data
