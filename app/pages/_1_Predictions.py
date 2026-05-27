import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
import numpy as np

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AI Forecasting Dashboard",
    layout="wide"
)

# ==========================================
# LOAD MODEL
# ==========================================

model = joblib.load("../models/forecast_model.pkl")

# ==========================================
# PAGE TITLE
# ==========================================

st.title("📈 AI Course Demand & Revenue Forecasting")

st.markdown("""
Predict future enrollments, course demand,
and revenue using Artificial Intelligence
and Machine Learning.
""")

st.markdown("---")

# ==========================================
# INPUT SECTION
# ==========================================

st.subheader("📌 Course Configuration")

col1, col2 = st.columns(2)

with col1:

    course_price = st.slider(
        "💰 Course Price (₹)",
        0,
        10000,
        3000
    )

    course_duration = st.slider(
        "⏱️ Course Duration",
        1,
        52,
        12
    )

    course_rating = st.slider(
        "⭐ Course Rating",
        1.0,
        5.0,
        4.0
    )

with col2:

    duration_unit = st.selectbox(
        "📅 Duration Unit",
        ["Days", "Weeks", "Months"]
    )

    teacher_rating = st.slider(
        "👨‍🏫 Teacher Rating",
        1.0,
        5.0,
        4.2
    )

    experience = st.slider(
        "💼 Years of Experience",
        1,
        20,
        5
    )

# ==========================================
# CONVERT DURATION
# ==========================================

if duration_unit == "Days":

    duration_value = course_duration

elif duration_unit == "Weeks":

    duration_value = course_duration * 7

else:

    duration_value = course_duration * 30

# ==========================================
# BUTTON
# ==========================================

st.markdown("<br>", unsafe_allow_html=True)

run_forecast = st.button(
    "🚀 Run AI Forecast",
    use_container_width=True
)

# ==========================================
# PREDICTION SECTION
# ==========================================

if run_forecast:

    # ======================================
    # MODEL INPUT
    # ======================================

    input_data = np.array([[
        1,
        1,
        1,
        course_price,
        duration_value,
        course_rating,
        teacher_rating,
        experience,
        1,
        1,
        1
    ]])

    # ======================================
    # REAL MODEL PREDICTION
    # ======================================

    raw_prediction = abs(
        model.predict(input_data)[0]
    )

    # ======================================
    # ENROLLMENT PREDICTION
    # ======================================

    enrollment_prediction = int(

        raw_prediction

        + (course_rating * 25)

        + (teacher_rating * 20)

        + (experience * 5)

        - (course_price / 400)

        + (duration_value / 5)

    )

    # MINIMUM ENROLLMENTS

    enrollment_prediction = max(
        enrollment_prediction,
        25
    )

    # ======================================
    # REVENUE PREDICTION
    # ======================================

    revenue_prediction = int(
        enrollment_prediction * course_price
    )

    # ======================================
    # DYNAMIC DEMAND SCORE
    # ======================================

    demand_score = int(

        (
            (course_rating * 20)
            +
            (teacher_rating * 18)
            +
            (experience * 2)
            +
            (duration_value / 10)
            +
            (enrollment_prediction / 8)
            -
            (course_price / 500)

        )

    )

    # LIMIT SCORE

    demand_score = max(
        min(demand_score, 100),
        1
    )

    # ======================================
    # SUCCESS PROBABILITY
    # ======================================

    success_probability = min(

        int(

            (
                course_rating * 10
                +
                teacher_rating * 10
                +
                experience
            ) * 1.5

        ),

        100

    )

    # ======================================
    # RISK LEVEL
    # ======================================

    if demand_score >= 80:

        risk_level = "Low Risk ✅"

    elif demand_score >= 50:

        risk_level = "Moderate Risk ⚠️"

    else:

        risk_level = "High Risk ❌"

    # ======================================
    # MARKET STATUS
    # ======================================

    if demand_score >= 85:

        market_status = "🔥 Highly Trending"

    elif demand_score >= 60:

        market_status = "📈 Growing Market"

    else:

        market_status = "📉 Competitive Market"

    # ======================================
    # RESULTS SECTION
    # ======================================

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
            "💰 Revenue Forecast",
            f"₹ {revenue_prediction}"
        )

    with col3:

        st.metric(
            "🔥 Demand Score",
            f"{demand_score}%"
        )

    st.markdown("---")

    # ======================================
    # BUSINESS INTELLIGENCE
    # ======================================

    st.subheader("🧠 AI Business Intelligence")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.info(f"""

        🎯 Success Probability

        {success_probability}%

        """)

    with col2:

        st.warning(f"""

        ⚠️ Business Risk

        {risk_level}

        """)

    with col3:

        st.success(f"""

        🚀 Market Trend

        {market_status}

        """)

    st.markdown("---")

    # ======================================
    # FORECAST VISUALIZATION
    # ======================================

    forecast_df = pd.DataFrame({

        "Metric": [

            "Enrollments",
            "Revenue",
            "Demand Score",
            "Success Probability"

        ],

        "Value": [

            enrollment_prediction,
            revenue_prediction,
            demand_score,
            success_probability

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

        template="plotly_dark",

        title="📈 AI Forecast Analytics"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ======================================
    # FUTURE GROWTH
    # ======================================

    st.markdown("---")

    st.subheader("🔮 Future Demand Growth")

    growth_df = pd.DataFrame({

        "Year": [
            2025,
            2026,
            2027,
            2028
        ],

        "Projected Enrollments": [

            enrollment_prediction,

            int(enrollment_prediction * 1.2),

            int(enrollment_prediction * 1.5),

            int(enrollment_prediction * 1.8)

        ]

    })

    growth_fig = px.line(

        growth_df,

        x="Year",
        y="Projected Enrollments",

        markers=True

    )

    growth_fig.update_layout(
        template="plotly_dark"
    )

    st.plotly_chart(
        growth_fig,
        use_container_width=True
    )

    # ======================================
    # AI RECOMMENDATIONS
    # ======================================

    st.markdown("---")

    st.subheader("🤖 AI Strategic Recommendations")

    if demand_score >= 80:

        st.success("""

        ✅ Excellent market opportunity detected.

        Recommended Actions:

        • Launch immediately
        • Increase marketing budget
        • Add certifications
        • Expand instructor hiring

        """)

    elif demand_score >= 50:

        st.warning("""

        ⚠️ Moderate market opportunity.

        Recommended Actions:

        • Improve ratings
        • Optimize pricing
        • Add industry projects
        • Improve course quality

        """)

    else:

        st.error("""

        ❌ High competition detected.

        Recommended Actions:

        • Rework course structure
        • Improve teacher profile
        • Reduce pricing
        • Focus on niche audience

        """)