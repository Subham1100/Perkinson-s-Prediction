#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 02:22:01 2023

@author: subhamchauhan
"""

import numpy as np
import pickle
import streamlit as st 
from streamlit_option_menu import option_menu 

loaded_model = pickle.load(open('/Users/subhamchauhan/Desktop/DiseasePrediction/trained_model','rb'))

def perkinsons(input_data):
    input_data_as_numpy_array =np.asarray(input_data)

    input_data_reshaped =input_data_as_numpy_array.reshape(1,-1)


    prediction = loaded_model.predict(input_data_reshaped)#here use use our loaded model
    print (prediction)
    if(prediction[0]==0):
      return("The person does not have parkinsons disease")
    else :
      return("The person does have parkinsons disease")
  
def main():
    st.title("Parkinson's Prediction")
    
    MDVP_Fo_Hz = st.text_input("MDVP:Fo(Hz) - Average vocal fundamental frequency")
    MDVP_Fhi_Hz = st.text_input("MDVP:Fhi(Hz) - Maximum vocal fundamental frequency")
    MDVP_Flo_Hz = st.text_input("MDVP:Flo(Hz) - Minimum vocal fundamental frequency")
    MDVP_Jitter = st.text_input("MDVP:Jitter(%)")
    MDVP_Jitter_Abs = st.text_input("MDVP:Jitter(Abs)")
    MDVP_RAP = st.text_input("MDVP:RAP")
    MDVP_PPQ = st.text_input("MDVP:PPQ")
    Jitter_DDP = st.text_input("Jitter:DDP - Several measures of variation in fundamental frequency")
    MDVP_Shimmer = st.text_input("MDVP:Shimmer")
    MDVP_Shimmer_dB = st.text_input("MDVP:Shimmer(dB)")
    Shimmer_APQ3 = st.text_input("Shimmer:APQ3")
    Shimmer_APQ5 = st.text_input("Shimmer:APQ5")
    MDVP_APQ = st.text_input("MDVP:APQ")
    Shimmer_DDA = st.text_input("Shimmer:DDA - Several measures of variation in amplitude")
    NHR = st.text_input("NHR")
    HNR = st.text_input("HNR - Two measures of ratio of noise to tonal components in the voice")
    RPDE = st.text_input("RPDE")
    D2 = st.text_input("D2 - Two nonlinear dynamical complexity measures")
    DFA = st.text_input("DFA - Signal fractal scaling exponent")
    spread1 = st.text_input("spread1")
    spread2 = st.text_input("spread2")
    PPE = st.text_input("PPE - Three nonlinear measures of fundamental frequency variation")
    
    diagnosis = ''
     
    if st.button('Test'):
        diagnosis = perkinsons([MDVP_Fo_Hz, MDVP_Fhi_Hz, MDVP_Flo_Hz, MDVP_Jitter, MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE])
     
    st.success(diagnosis)

     
 
    
if __name__ =='__main__':
    main()
     
     
     
     
     
     
     
     
     
     
     