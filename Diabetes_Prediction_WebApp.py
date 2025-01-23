# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 21:56:25 2025

@author: Nishant
"""

import numpy as np
import pandas as pd
import pickle
import streamlit as st

import os

# Loading the saved model
# Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to the model file
model_path = os.path.join(current_dir, 'trained_model.sav')
loaded_model = pickle.load(open(model_path, 'rb'))
# Function for prediction
def predict_diabetes(input_data):
    # Reshape the array for a single prediction
    input_data_reshaped = np.array(input_data).reshape(1, -1)
    
    # Predict using the trained model
    prediction = loaded_model.predict(input_data_reshaped)
    
    if prediction[0] == 0:
        return "The person is NOT diabetic."
    else:
        return "The person IS diabetic."

def main():
    # Title of the web app
    st.title('Diabetes Prediction Web App')
    
    # Getting user inputs
    Pregnancies = st.number_input("Number of Pregnancies:")
    Glucose = st.number_input("Glucose Level:")
    BloodPressure = st.number_input("Blood Pressure Value:")
    SkinThickness = st.number_input("Skin Thickness Value:")
    Insulin = st.number_input("Insulin Level:")
    BMI = st.number_input("BMI Value:")
    DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function Value:")
    Age = st.number_input("Age:")

    # Prediction result
    diagnosis = ''
    
    # Button for prediction
    if st.button('Diabetes Test Result'):
        input_data = [
            Pregnancies, Glucose, BloodPressure, SkinThickness,
            Insulin, BMI, DiabetesPedigreeFunction, Age
        ]
        diagnosis = predict_diabetes(input_data)
        
    st.success(diagnosis)

if __name__ == '__main__':
    main()
