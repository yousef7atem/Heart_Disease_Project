import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load('../models/final_model.pkl')

st.title("Heart Disease Prediction App")

st.sidebar.header("Input Patient Data")

def user_input_features():
    age = st.sidebar.slider('Age', 29, 77, 45)
    cp = st.sidebar.selectbox('Chest Pain Type', [0,1,2,3])
    trestbps = st.sidebar.slider('Resting Blood Pressure', 94, 200, 130)
    chol = st.sidebar.slider('Cholesterol', 126, 564, 250)
    thalach = st.sidebar.slider('Max Heart Rate Achieved', 71, 202, 150)
    exang = st.sidebar.selectbox('Exercise Induced Angina', [0,1])
    oldpeak = st.sidebar.slider('ST Depression', 0.0, 6.2, 1.0)
    slope = st.sidebar.selectbox('Slope of ST segment', [0,1,2])
    ca = st.sidebar.selectbox('Number of major vessels colored by fluoroscopy', [0,1,2,3,4])
    thal = st.sidebar.selectbox('Thalassemia', [0,1,2,3])
    
    data = {
        'age': age,
        'cp': cp,
        'trestbps': trestbps,
        'chol': chol,
        'thalach': thalach,
        'exang': exang,
        'oldpeak': oldpeak,
        'slope': slope,
        'ca': ca,
        'thal': thal
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

st.subheader('Patient Input Parameters')
st.write(input_df)

prediction = model.predict(input_df)
prediction_proba = model.predict_proba(input_df)

st.subheader('Prediction')
st.write('Heart Disease' if prediction[0]==1 else 'No Heart Disease')

st.subheader('Prediction Probability')
st.write(prediction_proba)
