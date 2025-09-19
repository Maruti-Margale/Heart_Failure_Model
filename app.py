import streamlit as st
import pickle
import numpy as np

# Load the model
with open("Heart_Failure_Prediction.pkl", "rb") as f:
    model = pickle.load(f)

# Page config
st.set_page_config(page_title="Heart Disease Prediction", layout="centered")

# Inject custom CSS
st.markdown("""
    <style>
    /* Navigation Bar */
    .navbar {
        background-color: #002B5B;
        padding: 1rem;
        text-align: center;
        color: white;
        font-size: 24px;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: #002B5B;
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 14px;
    }
    .stButton button {
        background-color: #005f73;
        color: white;
        border: none;
        padding: 0.6em 1em;
        border-radius: 5px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Navbar
st.markdown('<div class="navbar">💓 Heart Disease Risk Predictor</div>', unsafe_allow_html=True)

# Input UI
st.subheader("📝 Patient Information")

age = st.slider("Age", 18, 100, 50)
sex = st.selectbox("Sex", ["Female", "Male"])
resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 600, 200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL?", ["No", "Yes"])
resting_ecg = st.slider("Resting ECG (encoded value)", 0.0, 1.0, 0.5)
max_hr = st.slider("Max Heart Rate", 60, 210, 140)
exercise_angina = st.selectbox("Exercise-induced Angina", ["No", "Yes"])
oldpeak = st.slider("Oldpeak (ST depression)", 0.0, 6.5, 1.0)
st_slope = st.slider("ST Slope (encoded value)", 0.0, 1.0, 0.5)
chest_pain_type = st.selectbox("Chest Pain Type", ["ASY", "ATA", "NAP"])

# Encode fields
def encode(val): return 1 if val in ["Yes", "Male"] else 0
sex = encode(sex)
fasting_bs = encode(fasting_bs)
exercise_angina = encode(exercise_angina)

# One-hot for chest pain
chest_pain_asy = 1 if chest_pain_type == "ASY" else 0
chest_pain_ata = 1 if chest_pain_type == "ATA" else 0
chest_pain_nap = 1 if chest_pain_type == "NAP" else 0

# Feature vector
input_data = np.array([[
    age, sex, resting_bp, cholesterol, fasting_bs,
    resting_ecg, max_hr, exercise_angina, oldpeak, st_slope,
    chest_pain_asy, chest_pain_ata, chest_pain_nap
]])

# Predict
if st.button("🔍 Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("⚠️ High risk of heart disease. Please consult a doctor.")
    else:
        st.success("✅ Low risk of heart disease. Keep it up!")

# Footer
st.markdown('<div class="footer">Made with ❤️ using Streamlit</div>', unsafe_allow_html=True)
