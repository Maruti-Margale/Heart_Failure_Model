import streamlit as st
import pickle
import numpy as np

# Load model
with open("Heart_Failure_Prediction.pkl", "rb") as f:
    model = pickle.load(f)

# Set page layout
st.set_page_config(page_title="Heart Disease Prediction", layout="centered")

# Custom CSS with new color scheme
st.markdown("""
    <style>
    .navbar {
        background-color: #4B0082;
        padding: 1rem;
        text-align: center;
        color: #ffffff;
        font-size: 26px;
        border-radius: 8px;
        margin-bottom: 30px;
        font-weight: bold;
    }
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: #2F4F4F;
        color: #ffffff;
        text-align: center;
        padding: 12px;
        font-size: 13px;
        border-top: 1px solid #444;
    }
    .stButton button {
        background-color: #2E8B57;
        color: white;
        font-weight: bold;
        padding: 0.6em 1.2em;
        border-radius: 6px;
        border: none;
        font-size: 16px;
    }
    .stButton button:hover {
        background-color: #276749;
        transition: 0.3s;
    }
    </style>
""", unsafe_allow_html=True)

# Navbar
st.markdown('<div class="navbar">💓 Heart Disease Risk Predictor</div>', unsafe_allow_html=True)

# Input fields
st.subheader("📝 Patient Information")

age = st.slider("Age", 18, 100, 50)
sex = st.selectbox("Sex", ["Female", "Male"])
resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 600, 200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL?", ["No", "Yes"])
resting_ecg = st.slider("Resting ECG Risk Value", 0.0, 1.0, 0.5)
max_hr = st.slider("Max Heart Rate", 60, 210, 140)
exercise_angina = st.selectbox("Exercise-induced Angina", ["No", "Yes"])
oldpeak = st.slider("Oldpeak (ST depression)", 0.0, 6.5, 1.0)
st_slope = st.slider("ST Slope Risk Value", 0.0, 1.0, 0.5)
chest_pain_type = st.selectbox("Chest Pain Type", ["ASY", "ATA", "NAP", "TA"])

# Encoding
def encode(val):
    return 1 if val in ["Yes", "Male"] else 0

sex = encode(sex)
fasting_bs = encode(fasting_bs)
exercise_angina = encode(exercise_angina)

# One-hot encoding for ChestPainType
chest_pain_asy = 1 if chest_pain_type == "ASY" else 0
chest_pain_ata = 1 if chest_pain_type == "ATA" else 0
chest_pain_nap = 1 if chest_pain_type == "NAP" else 0
chest_pain_ta = 1 if chest_pain_type == "TA" else 0

# Final input
input_data = np.array([[
    age, sex, resting_bp, cholesterol, fasting_bs,
    resting_ecg, max_hr, exercise_angina, oldpeak, st_slope,
    chest_pain_asy, chest_pain_ata, chest_pain_nap, chest_pain_ta
]])

# Predict button
if st.button("🔍 Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("⚠️ High risk of heart disease. Please consult a doctor.")
    else:
        st.success("✅ Low risk of heart disease. Keep up the good lifestyle!")

# Footer
st.markdown('<div class="footer">Made with ❤️ by Maruti | Powered by Streamlit</div>', unsafe_allow_html=True)
