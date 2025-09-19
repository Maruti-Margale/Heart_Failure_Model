import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("Heart_Failure_Prediction.pkl", "rb") as file:
    model = pickle.load(file)

st.title("💓 Heart Failure Prediction App")
st.write("Enter the details below to predict the risk of heart failure:")

# Input fields
age = st.slider("Age", 18, 100, 50)
anaemia = st.selectbox("Anaemia", ["No", "Yes"])
creatinine_phosphokinase = st.number_input("Creatinine Phosphokinase (mcg/L)", 23, 7861, 250)
diabetes = st.selectbox("Diabetes", ["No", "Yes"])
ejection_fraction = st.slider("Ejection Fraction (%)", 10, 80, 40)
high_blood_pressure = st.selectbox("High Blood Pressure", ["No", "Yes"])
platelets = st.number_input("Platelets (kiloplatelets/mL)", 25000, 850000, 265000)
serum_creatinine = st.number_input("Serum Creatinine (mg/dL)", 0.5, 10.0, 1.1)
serum_sodium = st.number_input("Serum Sodium (mEq/L)", 100, 150, 137)
sex = st.selectbox("Sex", ["Female", "Male"])
smoking = st.selectbox("Smoking", ["No", "Yes"])
time = st.slider("Follow-up Period (in days)", 0, 300, 130)

# Map categorical values
def map_input(value):
    return 1 if value == "Yes" or value == "Male" else 0

input_data = np.array([
    age,
    map_input(anaemia),
    creatinine_phosphokinase,
    map_input(diabetes),
    ejection_fraction,
    map_input(high_blood_pressure),
    platelets,
    serum_creatinine,
    serum_sodium,
    map_input(sex),
    map_input(smoking),
    time
]).reshape(1, -1)

# Predict button
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("⚠️ High risk of heart failure. Please consult a doctor.")
    else:
        st.success("✅ Low risk of heart failure.")
