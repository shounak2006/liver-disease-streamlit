import streamlit as st
import numpy as np
import joblib

model = joblib.load("rf_liver_model.pkl")

st.set_page_config(page_title="Liver Disease Prediction")

st.title("Liver Disease Prediction System")
# -----------------------------
# User Input Section
# -----------------------------
NORMAL_RANGES = {
    "Age (years)": "18–65",
    "Total Bilirubin (mg/dL)": "0.1–1.2",
    "Direct Bilirubin (mg/dL)": "0.0–0.3",
    "Total Proteins (g/dL)": "6.0–8.3",
    "Albumin (g/dL)": "3.5–5.0",
    "A/G Ratio": "1.0–2.5",
    "SGPT / ALT (U/L)": "7–56",
    "SGOT / AST (U/L)": "10–40",
    "Alkaline Phosphatase (U/L)": "44–147",
}

age = st.number_input("Age", min_value=1, max_value=120)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

tot_bilirubin = st.number_input("Total Bilirubin")
direct_bilirubin = st.number_input("Direct Bilirubin")
tot_proteins = st.number_input("Total Proteins")
albumin = st.number_input("Albumin")
ag_ratio = st.number_input("Albumin–Globulin Ratio")
sgpt = st.number_input("SGPT")
sgot = st.number_input("SGOT")
alkphos = st.number_input("Alkaline Phosphatase")

# -----------------------------
# Encode gender (AFTER input)
# -----------------------------
gender_val = 1 if gender == "Male" else 0


input_data = np.array([[
    age, gender_val, tot_bilirubin, direct_bilirubin,
    tot_proteins, albumin, ag_ratio, sgpt, sgot, alkphos
]])

if st.button("Predict"):
    pred = model.predict(input_data)
    prob = model.predict_proba(input_data)

    if pred[0] == 1:
        st.error("Liver Disease Detected")
    else:
        st.success("No Liver Disease Detected")

    st.write("Probability:", round(prob[0][1]*100, 2), "%")

st.caption("Academic demonstration only")
