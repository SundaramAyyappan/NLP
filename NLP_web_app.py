# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 16:24:51 2023

@author: Jeevika
"""

import numpy as np
import pandas as pd
import pickle
import streamlit as st

loaded_model = pickle.load(open("E:/Userfiles/Desktop/Python/project/Sentiment1.sav",'rb'))


st.title('emotion Prediction Web App')
st.sidebar.header('User Input Parameters')

def user_input_features():
    Lemma_text = st.text_input('Enter a comment')
    
    data = {'Comments': Lemma_text}
    features = pd.DataFrame(data,index = [0])
    return features 

sub = user_input_features()
st.subheader('User Input parameters')
st.write(sub)


st.write('Your comment is classified as', sub)



