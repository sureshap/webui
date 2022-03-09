
#Necessary imports
import streamlit as st
import pandas as pd
import numpy as np # linear algebra
#import matplotlib.pyplot as plt # plotting graph for EDA , Metrics analysis

from textblob import TextBlob
from collections import Counter


#Headings for Web Application
st.title("Natural Language Processing Web Application Example")
st.subheader("What type of NLP service would you like to use?")

#Picking what NLP task you want to do
option = st.selectbox('NLP Service',('Sentiment Analysis', 'Entity Extraction', 'Text Summarization')) #option is stored in this variable

#Textbox for text user is entering
st.subheader("Enter the text you'd like to analyze.")
text = st.text_input('Enter text') #text is stored in this variable

#Display results of the NLP task
st.header("Results")

#Function to take in dictionary of entities, type of entity, and returns specific entities of specific type
def entRecognizer(entDict, typeEnt):
    entList = [ent for ent in entDict if entDict[ent] == typeEnt]
    return entList


#Sentiment Analysis
if option == 'Sentiment Analysis':
    st.write("The sentiment of the overall text below.")


#Named Entity Recognition
elif option == 'Entity Extraction':


    #Displaying entities of each type
    st.write("Entity Extraction")


#Text Summarization
else:
    st.subheader("Summary")

