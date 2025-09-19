import streamlit as st

st.set_page_config(page_title="About", layout="centered")

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
    </style>
    <div class="navbar">ℹ️ About the Project</div>
""", unsafe_allow_html=True)

st.write("""
This app predicts the risk of heart disease using a machine learning model trained on clinical patient data.

### 🔬 Model Info:
- **Algorithm**: K-Nearest Neighbors
- **Features Used**: 14 (vitals + categorical + encoded)
- **Target**: Heart Disease (Yes/No)

### 📊 Data Source:
The data used for this project was based on anonymized heart patient records.

### 👨‍💻 Built By:
- Maruti
- Powered by Python, Streamlit, Scikit-learn
""")
