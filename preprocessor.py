import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# =====================================================
# LOAD MODEL
# =====================================================

model = joblib.load(
    "../model/random_forest_model.pkl"
)

# =====================================================
# PAGE TITLE
# =====================================================

st.title("📈 AI Course Demand Prediction")

st.markdown("""
### 🚀 Real Machine Learning Forecasting System
""")

st.markdown("---")

# =====================================================
# INPUT SECTION
# =====================================================

st.subheader("📌 Course Configuration")

col1, col2 = st.columns(2)

with col1:

    course_price = st.slider(

        "💰 Course Price",

        0,
        10000,
        3000

    )

    course_duration = st.slider(

        "📅 Course Duration (Weeks)",

        1,
        52,
        8

    )

    course_rating = st.slider(

        "⭐ Course Rating",

        1.0,
        5.0,
        4.2

    )

with col2:

    teacher_rating = st.slider(

        "👨‍🏫 Teacher Rating",

        1.0,
        5.0,
        4.5

    )

    years_experience = st.slider(

        "🎯 Years Of Experience",

        1,
        20,
        5

    )

    course_level = st.selectbox(

        "📚 Course Level",

        [0, 1, 2]

    )

# =====================================================
# FEATURE ENGINEERING
# =====================================================

if course_price == 0:
    price_band = 0

elif course_price < 2000:
    price_band = 1

elif course_price < 5000:
    price_band = 2

else:
    price_band = 3

if years_experience < 3:
    exp_level = 0

elif years_experience < 8:
    exp_level = 1

else:
    exp_level = 2

if teacher_rating < 2:
    rating_tier = 0

elif teacher_rating < 4:
    rating_tier = 1

else:
    rating_tier = 2

# =====================================================
# PREDICT BUTTON
# =====================================================

if st.button("🚀 Run AI Forecast"):

    input_data = pd.DataFrame({

        "CourseCategory": [1],
        "CourseType": [1],
        "CourseLevel": [course_level],
        "CoursePrice": [course_price],
        "CourseDuration": [course_duration],
        "CourseRating": [course_rating],
        "TeacherRating": [teacher_rating],
        "YearsOfExperience": [years_experience],
        "PriceBand": [price_band],
        "ExperienceLevel": [exp_level],
        "RatingTier": [rating_tier]

    })

    prediction = model.predict(input_data)[0]

    # ==============================================
    # SAFE PREDICTIONS
    # ==============================================

    enrollment_prediction = max(
        int(prediction),
        1
    )

    revenue_prediction = max(
        int(enrollment_prediction * course_price),
        1000
    )

    demand_score = min(
        int((enrollment_prediction / 100) * 100),
        100
    )

    st.markdown("---")

    st.subheader("📊 AI Forecast Results")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(

            "👨‍🎓 Predicted Enrollments",

            enrollment_prediction

        )

    with col2:

        st.metric(

            "💰 Revenue Potential",

            f"₹ {revenue_prediction}"

        )

    with col3:

        st.metric(

            "🔥 Demand Score",

            f"{demand_score}%"

        )

    st.markdown("---")

    # ==============================================
    # VISUALIZATION
    # ==============================================

    forecast_df = pd.DataFrame({

        "Metric": [

            "Enrollments",
            "Revenue",
            "Demand Score"

        ],

        "Value": [

            enrollment_prediction,
            revenue_prediction,
            demand_score

        ]

    })

    fig = px.bar(

        forecast_df,

        x="Metric",
        y="Value",

        color="Metric",

        text="Value"

    )

    fig.update_layout(

        template="plotly_dark"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ==============================================
    # AI INSIGHTS
    # ==============================================

    st.subheader("🧠 AI Recommendations")

    if demand_score > 80:

        st.success("""

        ✅ High demand course detected.

        Recommended for immediate launch.

        """)

    elif demand_score > 50:

        st.warning("""

        ⚠️ Moderate demand detected.

        Improve ratings and pricing strategy.

        """)

    else:

        st.error("""

        ❌ Low demand probability.

        Consider redesigning course structure.

        """)