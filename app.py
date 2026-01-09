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

import streamlit as st
import numpy as np
import joblib

model = joblib.load("rf_liver_model.pkl")

st.set_page_config(page_title="Liver Disease Prediction")

st.title("Liver Disease Prediction System")
st.write("Machine Learning based prediction (Academic Use Only)")

age = st.number_input("Age", min_value=1, max_value=120, help=NORMAL_RANGES["Age (years)"])
tot_bilirubin = st.number_input("Total Bilirubin", help=NORMAL_RANGES["Total Bilirubin (mg/dL)"])
direct_bilirubin = st.number_input("Direct Bilirubin", help=NORMAL_RANGES["Direct Bilirubin (mg/dL)"])
tot_proteins = st.number_input("Total Proteins", help=NORMAL_RANGES["Total Proteins (g/dL)"])
albumin = st.number_input("Albumin", help=NORMAL_RANGES["Albumin (g/dL)"])
ag_ratio = st.number_input("Albumin–Globulin Ratio", help=NORMAL_RANGES["A/G Ratio"])
sgpt = st.number_input("SGPT", help=NORMAL_RANGES["SGPT / ALT (U/L)"])
sgot = st.number_input("SGOT", help=NORMAL_RANGES["SGOT / AST (U/L)"])
alkphos = st.number_input("Alkaline Phosphatase", help=NORMAL_RANGES["Alkaline Phosphatase (U/L)"])




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
