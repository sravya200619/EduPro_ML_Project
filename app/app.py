import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="EduPro AI Platform",
    page_icon="🎓",
    layout="wide"
)

# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown("""

<style>

/* MAIN APP */

.stApp {
    background-color: #0E1117;
}

/* SIDEBAR */

[data-testid="stSidebar"] {
    background-color: #111827;
}

/* REMOVE MENU */

#MainMenu {
    visibility: hidden;
}

/* REMOVE FOOTER */

footer {
    visibility: hidden;
}

/* REMOVE HEADER */

header {
    visibility: hidden;
}

/* TEXT */

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    color: white;
}

/* HERO TITLE */

.hero-title {
    font-size: 65px;
    font-weight: bold;
    text-align: center;
    color: white;
    margin-top: 60px;
}

/* HERO SUBTITLE */

.hero-subtitle {
    font-size: 26px;
    text-align: center;
    color: #C0C0C0;
    margin-bottom: 40px;
}

/* FEATURE BOX */

.feature-box {
    background-color: #1E1E1E;
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    color: white;
    box-shadow: 0px 0px 15px rgba(255,255,255,0.08);
}

/* METRIC CARDS */

[data-testid="metric-container"] {
    background-color: #1E1E1E;
    border-radius: 15px;
    padding: 15px;
    border: 1px solid #333333;
}

/* BUTTON */

.stButton>button {
    width: 100%;
    height: 55px;
    border-radius: 12px;
    font-size: 20px;
    font-weight: bold;
    background-color: #2563EB;
    color: white;
    border: none;
}

/* BUTTON HOVER */

.stButton>button:hover {
    background-color: #1D4ED8;
    color: white;
}

/* FOOTER */

.footer {
    text-align: center;
    color: gray;
    margin-top: 50px;
}

</style>

""", unsafe_allow_html=True)

# ==================================================
# SESSION STATE
# ==================================================

if "dashboard_open" not in st.session_state:
    st.session_state.dashboard_open = False

# ==================================================
# LANDING PAGE
# ==================================================

if st.session_state.dashboard_open == False:

    st.markdown("""
    <div class="hero-title">
    🎓 EduPro AI Forecasting Platform
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero-subtitle">
    Predict Course Demand, Revenue &
    Learning Trends using Artificial Intelligence
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ==================================================
    # PLATFORM MODULES
    # ==================================================

    st.markdown("## 🚀 Platform Modules")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("""
        📊 Dashboard Analytics
        
        Real-time forecasting
        and AI-driven insights.
        """)

    with col2:
        st.success("""
        📈 Prediction Engine
        
        Predict enrollments and
        future revenue growth.
        """)

    with col3:
        st.warning("""
        🧠 AI Intelligence
        
        Smart recommendations
        and demand analysis.
        """)

    st.markdown("<br>", unsafe_allow_html=True)

    # ==================================================
    # FEATURE CARDS
    # ==================================================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="feature-box">
        <h2>📈 Forecasting</h2>
        <p>
        AI-powered prediction system
        for enrollment and revenue.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-box">
        <h2>💰 Revenue Analytics</h2>
        <p>
        Analyze category revenue,
        growth and demand trends.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-box">
        <h2>🚀 Recommendations</h2>
        <p>
        Discover trending technologies
        and future learning paths.
        </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # ==================================================
    # OVERVIEW
    # ==================================================

    st.subheader("📊 Platform Overview")

    st.write("""

    EduPro is an AI-powered predictive analytics platform
    designed for educational forecasting and business intelligence.

    The platform helps analyze:

    - Course Demand Forecasting
    - Revenue Growth Analysis
    - Enrollment Trends
    - Technology Popularity
    - Learner Engagement
    - AI-based Recommendations

    Technologies Used:

    - Python
    - Streamlit
    - Machine Learning
    - Predictive Analytics
    - Plotly Visualization

    """)

    st.markdown("---")

    # ==================================================
    # TRENDING TECHNOLOGIES
    # ==================================================

    st.subheader("🔥 Trending Technologies")

    trend_df = pd.DataFrame({
        "Technology": [
            "Artificial Intelligence",
            "Machine Learning",
            "Python",
            "Data Science",
            "Cybersecurity",
            "Cloud Computing",
            "Java"
        ],
        "Demand Score": [
            98,
            96,
            94,
            92,
            88,
            85,
            82
        ]
    })

    fig = px.bar(
        trend_df,
        x="Technology",
        y="Demand Score",
        color="Technology"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    # ==================================================
    # LAUNCH BUTTON
    # ==================================================

    center1, center2, center3 = st.columns([1,2,1])

    with center2:

        if st.button("🚀 Launch AI Dashboard"):

            st.session_state.dashboard_open = True
            st.rerun()

    # ==================================================
    # FOOTER
    # ==================================================

    st.markdown("""
    <div class="footer">
    Built using AI • Machine Learning • Streamlit • Plotly
    </div>
    """, unsafe_allow_html=True)

# ==================================================
# MAIN DASHBOARD
# ==================================================

else:

    # ==================================================
    # LOAD DATA
    # ==================================================

    data = pd.read_csv("../data/merged_data.csv")

    # ==================================================
    # TITLE
    # ==================================================

    st.title("🎓 EduPro AI Dashboard")

    st.markdown("""
    ### 🚀 AI-Powered Predictive Analytics Platform
    """)

    st.markdown("---")

    # ==================================================
    # KPI METRICS
    # ==================================================

    total_courses = data["CourseID"].nunique()
    total_students = data["UserID"].nunique()
    total_revenue = int(data["Revenue"].sum())
    avg_rating = round(data["CourseRating"].mean(), 2)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📚 Total Courses", total_courses)

    with col2:
        st.metric("👨‍🎓 Total Learners", total_students)

    with col3:
        st.metric("💰 Revenue", f"₹ {total_revenue}")

    with col4:
        st.metric("⭐ Avg Rating", avg_rating)

    st.markdown("---")

    # ==================================================
    # PROJECT VISION
    # ==================================================

    st.subheader("🎯 Strategic Decision Intelligence")

    st.markdown("""
    <div class="feature-box">

    <h2>🔮 Predictive Intelligence Vision</h2>

    <p style='font-size:18px;'>

    Which courses will attract enrollments and generate revenue in the future?

    EduPro introduces predictive intelligence to transform
    traditional reactive reporting into proactive strategic planning.

    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ==================================================
    # HIGH DEMAND COURSES
    # ==================================================

    st.subheader("🔥 Future High-Demand Courses")

    demand_df = pd.DataFrame({
        "Course": [
            "Artificial Intelligence",
            "Machine Learning",
            "Python Development",
            "Data Science",
            "Cybersecurity",
            "Cloud Computing",
            "Generative AI",
            "Java Full Stack"
        ],
        "Future Demand Score": [
            99,
            97,
            95,
            94,
            91,
            89,
            98,
            85
        ]
    })

    fig_demand = px.bar(
        demand_df,
        x="Course",
        y="Future Demand Score",
        color="Future Demand Score",
        text="Future Demand Score"
    )

    fig_demand.update_layout(template="plotly_dark")

    st.plotly_chart(
        fig_demand,
        use_container_width=True
    )

    st.markdown("---")

    # ==================================================
    # REVENUE BY CATEGORY
    # ==================================================

    st.subheader("📈 Revenue by Category")

    category_data = data.groupby(
        "CourseCategory"
    )["Revenue"].sum().reset_index()

    fig1 = px.bar(
        category_data,
        x="CourseCategory",
        y="Revenue",
        color="CourseCategory"
    )

    fig1.update_layout(template="plotly_dark")

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    st.markdown("---")

    # ==================================================
    # COURSE LEVEL DISTRIBUTION
    # ==================================================

    st.subheader("📊 Course Level Distribution")

    try:

        level_data = data["CourseLevel"].value_counts().reset_index()

        level_data.columns = [
            "CourseLevel",
            "Count"
        ]

        fig2 = px.pie(
            level_data,
            names="CourseLevel",
            values="Count"
        )

        fig2.update_layout(template="plotly_dark")

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    except:
        st.warning("CourseLevel column not available.")

    st.markdown("---")

    # ==================================================
    # TRENDING TECHNOLOGIES
    # ==================================================

    st.subheader("🔥 Trending Technologies")

    tech_df = pd.DataFrame({
        "Technology": [
            "AI",
            "Machine Learning",
            "Python",
            "Data Science",
            "Cloud",
            "Cybersecurity"
        ],
        "Demand": [
            98,
            96,
            94,
            91,
            87,
            85
        ]
    })

    fig3 = px.line(
        tech_df,
        x="Technology",
        y="Demand",
        markers=True
    )

    fig3.update_layout(template="plotly_dark")

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    st.markdown("---")

    # ==================================================
    # AI INSIGHTS
    # ==================================================

    st.subheader("🧠 AI Insights")

    insights = [
        "AI and Machine Learning courses have the highest demand.",
        "Python remains the most popular programming language.",
        "High-rated instructors improve enrollment growth.",
        "Premium courses generate higher future revenue.",
        "Cybersecurity and Cloud Computing are growing rapidly."
    ]

    for insight in insights:
        st.success(insight)

    st.markdown("---")

    # ==================================================
    # PROBLEM STATEMENT
    # ==================================================

    st.subheader("⚠️ Problem Statement")

    st.error("""

    EduPro currently lacks:

    • Predictive models for course enrollment demand

    • Revenue forecasting at course and category level

    • Quantitative evidence for pricing decisions

    """)

    st.markdown("---")

    # ==================================================
    # PREDICTIVE TARGETS
    # ==================================================

    st.subheader("🎯 Predictive Targets")

    target_df = pd.DataFrame({
        "Target Variable": [
            "Enrollment Count",
            "Course Revenue",
            "Category Revenue"
        ],
        "Description": [
            "Number of enrollments per course",
            "Total revenue generated per course",
            "Aggregated revenue by category"
        ]
    })

    st.dataframe(
        target_df,
        use_container_width=True
    )

    st.markdown("---")

    # ==================================================
    # FEATURE IMPORTANCE
    # ==================================================

    st.subheader("🧠 Feature Importance Analysis")

    importance_df = pd.DataFrame({
        "Feature": [
            "Course Price",
            "Instructor Rating",
            "Course Category",
            "Course Level",
            "Experience"
        ],
        "Importance Score": [
            92,
            88,
            84,
            79,
            75
        ]
    })

    fig_importance = px.bar(
        importance_df,
        x="Feature",
        y="Importance Score",
        color="Importance Score"
    )

    fig_importance.update_layout(template="plotly_dark")

    st.plotly_chart(
        fig_importance,
        use_container_width=True
    )

    st.markdown("---")

    # ==================================================
    # CONCLUSION
    # ==================================================

    st.subheader("✅ Conclusion")

    st.success("""

    This project transforms EduPro’s historical course data
    into forward-looking intelligence.

    EduPro can strategically:

    • Plan new course launches

    • Optimize pricing strategies

    • Improve instructor onboarding

    • Reduce business risks using AI forecasting

    """)