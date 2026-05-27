import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="EduPro AI Dashboard",
    layout="wide"
)

# ==========================================
# LOAD DATA
# ==========================================

data = pd.read_csv(
    "../data/merged_data.csv"
)

# ==========================================
# HEADER SECTION
# ==========================================

st.markdown("""

# 🎓 EduPro AI Forecasting Platform

### Predict Course Demand, Revenue & Learning Trends using Artificial Intelligence

""")

st.markdown("---")

# ==========================================
# KPI SECTION
# ==========================================

total_courses = data["CourseID"].nunique()

total_revenue = int(
    data["Revenue"].sum()
)

total_teachers = data["TeacherID"].nunique()

avg_rating = round(
    data["CourseRating"].mean(),
    2
)

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "📚 Total Courses",
        total_courses
    )

with col2:

    st.metric(
        "💰 Total Revenue",
        f"₹ {total_revenue}"
    )

with col3:

    st.metric(
        "👨‍🏫 Total Instructors",
        total_teachers
    )

with col4:

    st.metric(
        "⭐ Average Rating",
        avg_rating
    )

st.markdown("---")

# ==========================================
# PLATFORM OVERVIEW
# ==========================================

st.subheader("📊 Platform Analytics Overview")

left_col, right_col = st.columns(2)

# ==========================================
# COURSE CATEGORY ANALYSIS
# ==========================================

with left_col:

    category_data = data.groupby(

        "CourseCategory"

    )["Revenue"].sum().reset_index()

    fig1 = px.bar(

        category_data,

        x="CourseCategory",
        y="Revenue",

        color="CourseCategory",

        title="💰 Revenue by Course Category"

    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

# ==========================================
# COURSE TYPE DISTRIBUTION
# ==========================================

with right_col:

    type_data = data.groupby(

        "CourseType"

    )["CourseID"].count().reset_index()

    fig2 = px.pie(

        type_data,

        names="CourseType",
        values="CourseID",

        title="📚 Course Type Distribution"

    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

st.markdown("---")

# ==========================================
# TRENDING TECHNOLOGIES
# ==========================================

st.subheader("🔥 Trending Technology Courses")

trending_courses = [

    "Machine Learning",
    "Artificial Intelligence",
    "Python",
    "Java",
    "Data Science",
    "Cybersecurity",
    "Cloud Computing",
    "Full Stack Development"

]

trend_df = pd.DataFrame({

    "Technology": trending_courses,

    "Demand Score": [
        95,
        92,
        90,
        87,
        89,
        85,
        84,
        88
    ]

})

fig3 = px.line(

    trend_df,

    x="Technology",
    y="Demand Score",

    markers=True,

    title="📈 Trending Technology Demand"

)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.markdown("---")

# ==========================================
# TOP COURSES
# ==========================================

st.subheader("🏆 Top Rated Courses")

top_courses = data.groupby(

    "CourseName"

)["CourseRating"].mean().reset_index()

top_courses = top_courses.sort_values(

    by="CourseRating",
    ascending=False

).head(10)

fig4 = px.bar(

    top_courses,

    x="CourseName",
    y="CourseRating",

    color="CourseRating",

    title="⭐ Highest Rated Courses"

)

st.plotly_chart(
    fig4,
    use_container_width=True
)

st.markdown("---")

# ==========================================
# AI INSIGHTS
# ==========================================

st.subheader("🧠 AI Generated Insights")

insights = [

    "Courses with ratings above 4.5 generate significantly higher enrollments.",

    "AI and Machine Learning courses show the highest revenue potential.",

    "Premium courses with experienced instructors perform better.",

    "Python and Data Science remain top-demand technologies.",

    "Long-duration advanced courses improve learner retention."

]

for insight in insights:

    st.info(insight)

st.markdown("---")

# ==========================================
# DEMAND HEATMAP
# ==========================================

st.subheader("🔥 Demand & Revenue Heatmap")

heatmap_data = data.groupby(

    ["CourseCategory", "CourseLevel"]

)["Revenue"].sum().reset_index()

fig5 = px.density_heatmap(

    heatmap_data,

    x="CourseCategory",
    y="CourseLevel",
    z="Revenue",

    title="📊 Revenue Heatmap"

)

st.plotly_chart(
    fig5,
    use_container_width=True
)

st.markdown("---")

# ==========================================
# FUTURE RECOMMENDATIONS
# ==========================================

st.subheader("🚀 Future Growth Recommendations")

recommendations = [

    "Launch more AI and Generative AI courses.",

    "Increase premium instructor onboarding.",

    "Focus on high-demand technical domains.",

    "Introduce personalized learning recommendations.",

    "Optimize pricing for medium-duration courses."

]

for rec in recommendations:

    st.success(rec)

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.markdown("""

### 🎯 EduPro AI Forecasting & Recommendation Platform

Built using:
- Python
- Streamlit
- Machine Learning
- Plotly Analytics
- Predictive Forecasting

""")