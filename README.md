# Student GPA Predictor 🎓

**Predicts student GPA (0–4.0 scale)** using behavioral and socio-economic factors from the famous UCI Student Performance dataset (649 Portuguese students).

Live Demo → https://student-grade-predictor-muneebtalks.streamlit.app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://student-grade-predictor-muneebtalks.streamlit.app)

### Performance (Random Forest Regressor)
| Metric | Value     |
|-------|-----------|
| RMSE  | **0.35**  |
| R²    | **0.79**  |

Explains **79%** of the variance in student grades — excellent for a student project!

### Dataset
- Source: UCI Machine Learning Repository  
- Paper: Cortez and Silva, 2008  
- Link: https://archive.ics.uci.edu/dataset/320/student+performance  
- Features used: study time, failures, absences, parent education, alcohol consumption, health, family relations, extracurricular activities, etc.

### Tech Stack
- Python, pandas, scikit-learn  
- Random Forest Regressor (500 trees)  
- Streamlit for interactive web deployment  
- GitHub + Streamlit Community Cloud (free hosting)

### How to Run Locally
```bash
git clone https://github.com/muneebtalks/student-grade-predictor.git
cd student-grade-predictor
pip install -r requirements.txt   # (or manually: pandas, scikit-learn, streamlit, joblib)
streamlit run app.py