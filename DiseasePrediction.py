# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle
import streamlit as st 
from streamlit_option_menu import option_menu 
from sklearn.preprocessing import StandardScaler

loaded_model = pickle.load(open('/Users/subhamchauhan/Desktop/DiseasePrediction/trained_model','rb'))

input_data=(119.99200,157.30200,74.99700,0.00784,0.00007,0.00370,0.00554,0.01109,0.04374,0.42600,0.02182,0.03130,0.02971,0.06545,0.02211,21.03300,0.414783,0.815285,-4.813031,0.266482,2.301442,0.284654)#any random data
input_data_as_numpy_array =np.asarray(input_data)

input_data_reshaped =input_data_as_numpy_array.reshape(1,-1)


prediction = loaded_model.predict(input_data_reshaped)#here use use our loaded model
print (prediction)
if(prediction[0]==0):
  print("The person does not have parkinsons disease")
else :
  print("The person does have parkinsons disease")

