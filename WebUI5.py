

import streamlit as st
import numpy as np
import pandas as pd

# A function to load the data.
DATE_COLUMN = 'date/time'
DATA_URL = ('https://github.com/sureshap/webui/blob/main/input_data.xlsx')

st.write('Hello')

def load_data(nrows):
    data = pd.read_excel(DATA_URL, engine='openpyxl')
    return data
    

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
df_data = load_data(8500)
#df_data = pd.read_excel(DATA_URL)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

