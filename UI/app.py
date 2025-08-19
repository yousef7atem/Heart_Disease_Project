import streamlit as st
import pandas as pd
import joblib

# تحميل الموديل
model = joblib.load('best_heart_model.pkl')

st.title("Heart Disease Prediction")

# إدخال بيانات المستخدم
age = st.number_input("Age", 20, 100)
sex = st.selectbox("Sex", [0,1])
cp = st.selectbox("Chest Pain Type", [0,1,2,3])
trestbps = st.number_input("Resting Blood Pressure")
chol = st.number_input("Cholesterol")
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0,1])
restecg = st.selectbox("Resting ECG", [0,1,2])
thalach = st.number_input("Max Heart Rate")
exang = st.selectbox("Exercise Induced Angina", [0,1])
oldpeak = st.number_input("ST Depression")
slope = st.selectbox("Slope of ST", [0,1,2])
ca = st.selectbox("Number of Major Vessels", [0,1,2,3,4])
thal = st.selectbox("Thalassemia", [0,1,2,3])

# تجهيز البيانات
input_data = pd.DataFrame([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]],
                          columns=['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal'])

# زر التنبؤ
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.write(f"Predicted Heart Disease Class: {prediction[0]}")
