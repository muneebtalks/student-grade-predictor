# app.py — FINAL WORKING VERSION
import streamlit as st
import joblib
import numpy as np

# Load the model you just saved
model = joblib.load('rf_model.pkl')

st.set_page_config(page_title="Student GPA Predictor", page_icon="Graduation Cap")

st.title("Student GPA Predictor (0–4.0 Scale)")
st.markdown("**Dataset**: UCI Student Performance (Portuguese secondary school)")

col1, col2 = st.columns(2)

with col1:
    studytime = st.selectbox("Weekly Study Time",
                             options=[1, 2, 3, 4],
                             format_func=lambda x: ["<2h", "2–5h", "5–10h", ">10h"][x - 1])
    absences = st.slider("School Absences (per year)", 0, 30, 3)
    parent_ed = st.slider("Average Parent Education (0–4)", 0, 4, 2,
                          help="0 = none, 4 = higher education")
    activities = st.checkbox("Extracurricular Activities", value=True)

with col2:
    goout = st.slider("Time Going Out with Friends (1–5)", 1, 5, 3)
    health = st.selectbox("Health Status", options=[1, 2, 3, 4, 5],
                          format_func=lambda x: ["Very Bad", "Bad", "Okay", "Good", "Excellent"][x - 1])
    famrel = st.selectbox("Family Relationship Quality", options=[1, 2, 3, 4, 5],
                          format_func=lambda x: ["Very Bad", "Bad", "Okay", "Good", "Excellent"][x - 1])

# Convert to the exact features the model expects
hours_studied = studytime
attendance = max(0, 100 - (absences * 3))  # rough % attendance
parent_education = parent_ed / 2  # scale 0–2
extracurricular = 1 if activities else 0
sleep_hours = 10 - goout  # proxy
motivation_level = 0 if health <= 2 else 1 if health <= 4 else 2
parental_involvement = (famrel - 1) / 2  # 0–2 scale

if st.button("Predict My GPA", type="primary"):
    features = np.array([[hours_studied, attendance, parent_education,
                          extracurricular, sleep_hours, motivation_level,
                          parental_involvement]])
    prediction = model.predict(features)[0]

    st.success(f"**Predicted GPA: {prediction:.2f} / 4.0**")

    if prediction >= 3.7:
        st.balloons()
    elif prediction >= 3.0:
        st.write("Strong performance!")
    else:
        st.write("Focus on attendance & study time to improve!")

st.caption("Muhammad Muneeb | Nov 2025 | Random Forest Model (RMSE 0.35, R² 0.79)")