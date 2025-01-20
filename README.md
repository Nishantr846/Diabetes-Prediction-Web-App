# Diabetes-Prediction-Web-App


This repository contains the code for a **Diabetes Prediction Web App** built using **Streamlit** and a **machine learning model** for predicting diabetes. The web app allows users to input their health-related metrics, and based on these inputs, the trained model predicts whether they are diabetic or not.

## Features

- Interactive web interface built with **Streamlit**.
- Users can input health data such as pregnancies, glucose level, blood pressure, BMI, and more.
- Instant predictions using a **Support Vector Machine (SVM)** model trained on a diabetes dataset.
- The model predicts whether the user is diabetic or not based on the provided data.

## Technologies Used

- **Streamlit**: For building the web interface.
- **Python**: The programming language used.
- **Scikit-learn**: For implementing the machine learning model.
- **NumPy**: For numerical computations.
- **Pandas**: For data manipulation and loading the dataset.
- **Pickle**: For saving and loading the trained model.

## Setup and Installation

1. Clone the repository:
   git clone https://github.com/Nishantr846/diabetes-prediction-web-app.git

2. Navigate to the project folder:
   cd diabetes-prediction-web-app
3. Install the required dependencies:
   pip install pickle-mixin
   pip install scikit-learn
   pip install numpy
   pip install pandas
   pip install streamlit
4. Run the Streamlit app:
   streamlit run Diabetes_Prediction_WebApp.py

5. Open the app in your browser (Streamlit will provide a local URL).


## How It Works
The user inputs their health data into the provided fields on the web app (e.g., number of pregnancies, glucose level, blood pressure, etc.).
The machine learning model processes the inputs and predicts whether the user is diabetic or not.
The prediction result is displayed in real-time.


## Model Overview
The machine learning model is a Support Vector Machine (SVM) with a linear kernel, trained on the PIMA Indians Diabetes Database. The dataset includes health-related features such as:

- Number of Pregnancies
- Glucose Level
- Blood Pressure Value
- Skin Thickness Value
- Insulin Level
- BMI
- Diabetes Pedigree Function Value
- Age

The model was trained to predict whether a person has diabetes (Outcome: 1) or not (Outcome: 0).

## Saving and Loading the Model
The trained model is saved using Pickle to allow easy reuse without retraining the model each time.

1. Saving the Model:
   pickle.dump(model, open('trained_model.sav', 'wb'))
2. Loading the model:
   loaded_model = pickle.load(open('trained_model.sav', 'rb'))

# Contributing
Feel free to fork this project, submit issues, or create pull requests. Contributions are always welcome!

## Contact : 
Nishant Kumar
nishantr846@gmail.com
https://www.linkedin.com/in/nishantr846/



   


