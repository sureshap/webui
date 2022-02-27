

import streamlit as st
import numpy as np
import pandas as pd


x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)


y = st.button('Click') 

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option



if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

     chart_data
