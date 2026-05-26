import streamlit as st
import pandas as pd
import joblib

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="EduPro Forecasting Dashboard",
    layout="wide"
)

# =====================================
# LOAD MODEL
# =====================================

model = joblib.load(
    "../models/forecast_model.pkl"
)

# =====================================
# TITLE
# =====================================

st.title("📊 EduPro Demand & Revenue Forecasting")

st.markdown(
    "AI-powered course demand prediction dashboard"
)

# =====================================
# SIDEBAR INPUTS
# =====================================

st.sidebar.header("Course Details")

course_price = st.sidebar.slider(
    "Course Price",
    0,
    10000,
    3000
)

course_duration = st.sidebar.slider(
    "Course Duration",
    1,
    100,
    20
)

course_rating = st.sidebar.slider(
    "Course Rating",
    1.0,
    5.0,
    4.0
)

teacher_rating = st.sidebar.slider(
    "Teacher Rating",
    1.0,
    5.0,
    4.0
)

experience = st.sidebar.slider(
    "Years Of Experience",
    1,
    20,
    5
)

# =====================================
# SAMPLE INPUT DATA
# =====================================

input_data = pd.DataFrame({
    "CourseCategory": [0],
    "CourseType": [1],
    "CourseLevel": [0],
    "CoursePrice": [course_price],
    "CourseDuration": [course_duration],
    "CourseRating": [course_rating],
    "TeacherRating": [teacher_rating],
    "YearsOfExperience": [experience],
    "PriceBand": [1],
    "ExperienceLevel": [1],
    "RatingTier": [1]
})

# =====================================
# PREDICTION
# =====================================

prediction = model.predict(input_data)

# =====================================
# DISPLAY RESULTS
# =====================================

st.subheader("📈 Predicted Enrollment")

st.success(
    f"Expected Enrollment Count: {int(prediction[0])}"
)

# =====================================
# DATA VISUALIZATION
# =====================================

st.subheader("📊 Input Summary")

st.dataframe(input_data)