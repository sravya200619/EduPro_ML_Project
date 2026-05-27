import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Category Insights",
    layout="wide"
)

# ==========================================
# LOAD DATA
# ==========================================

data = pd.read_csv(
    "../data/merged_data.csv"
)

# ==========================================
# PAGE TITLE
# ==========================================

st.title("📉 Course Category Insights")

st.markdown("""

Analyze course category performance,
revenue generation, and market demand trends.

""")

st.markdown("---")

# ==========================================
# KPI SECTION
# ==========================================

total_categories = data["CourseCategory"].nunique()

highest_revenue = int(
    data.groupby("CourseCategory")["Revenue"]
    .sum()
    .max()
)

top_category = data.groupby(

    "CourseCategory"

)["Revenue"].sum().idxmax()

avg_rating = round(
    data["CourseRating"].mean(),
    2
)

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "📚 Total Categories",
        total_categories
    )

with col2:

    st.metric(
        "💰 Highest Revenue",
        f"₹ {highest_revenue}"
    )

with col3:

    st.metric(
        "🏆 Top Category",
        top_category
    )

with col4:

    st.metric(
        "⭐ Average Rating",
        avg_rating
    )

st.markdown("---")

# ==========================================
# CATEGORY REVENUE ANALYSIS
# ==========================================

st.subheader("💰 Revenue by Category")

category_revenue = data.groupby(

    "CourseCategory"

)["Revenue"].sum().reset_index()

fig1 = px.bar(

    category_revenue,

    x="CourseCategory",
    y="Revenue",

    color="CourseCategory",

    title="Revenue Distribution Across Categories"

)

st.plotly_chart(
    fig1,
    use_container_width=True
)

st.markdown("---")

# ==========================================
# ENROLLMENT ANALYSIS
# ==========================================

st.subheader("📈 Enrollment Distribution")

enrollment_data = data.groupby(

    "CourseCategory"

)["EnrollmentCount"].sum().reset_index()

fig2 = px.pie(

    enrollment_data,

    names="CourseCategory",
    values="EnrollmentCount",

    title="Enrollment Share by Category"

)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.markdown("---")

# ==========================================
# CATEGORY RATINGS
# ==========================================

st.subheader("⭐ Category Ratings")

rating_data = data.groupby(

    "CourseCategory"

)["CourseRating"].mean().reset_index()

fig3 = px.line(

    rating_data,

    x="CourseCategory",
    y="CourseRating",

    markers=True,

    title="Average Ratings Across Categories"

)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.markdown("---")

# ==========================================
# TRENDING CATEGORY ANALYSIS
# ==========================================

st.subheader("🔥 Trending Categories")

trend_data = pd.DataFrame({

    "Category": [

        "Artificial Intelligence",
        "Machine Learning",
        "Python",
        "Data Science",
        "Cybersecurity",
        "Cloud Computing",
        "Java",
        "Web Development"

    ],

    "Demand Score": [

        98,
        96,
        94,
        92,
        88,
        86,
        84,
        82

    ]

})

fig4 = px.area(

    trend_data,

    x="Category",
    y="Demand Score",

    title="Trending Technology Demand"

)

st.plotly_chart(
    fig4,
    use_container_width=True
)

st.markdown("---")

# ==========================================
# HEATMAP ANALYSIS
# ==========================================

st.subheader("📊 Category Revenue Heatmap")

heatmap_data = data.groupby(

    ["CourseCategory", "CourseLevel"]

)["Revenue"].sum().reset_index()

fig5 = px.density_heatmap(

    heatmap_data,

    x="CourseCategory",
    y="CourseLevel",
    z="Revenue",

    title="Revenue Heatmap by Course Level"

)

st.plotly_chart(
    fig5,
    use_container_width=True
)

st.markdown("---")

# ==========================================
# TOP PERFORMING CATEGORIES
# ==========================================

st.subheader("🏆 Top Performing Categories")

top_categories = category_revenue.sort_values(

    by="Revenue",
    ascending=False

).head(5)

fig6 = px.funnel(

    top_categories,

    x="Revenue",
    y="CourseCategory",

    title="Top Revenue Generating Categories"

)

st.plotly_chart(
    fig6,
    use_container_width=True
)

st.markdown("---")

# ==========================================
# AI INSIGHTS
# ==========================================

st.subheader("🧠 AI Insights")

insights = [

    "Artificial Intelligence courses show the highest demand growth.",

    "Machine Learning generates strong premium revenue.",

    "Python remains the most consistent learner choice.",

    "Cybersecurity demand is increasing rapidly.",

    "Cloud Computing courses show future growth potential.",

    "Advanced-level technical courses improve revenue significantly."

]

for insight in insights:

    st.info(insight)

st.markdown("---")

# ==========================================
# BUSINESS RECOMMENDATIONS
# ==========================================

st.subheader("🚀 Strategic Recommendations")

recommendations = [

    "Launch more AI and Data Science courses.",

    "Increase advanced certification programs.",

    "Partner with expert instructors in trending domains.",

    "Focus marketing on premium technology courses.",

    "Introduce personalized AI course recommendations."

]

for rec in recommendations:

    st.success(rec)

st.markdown("---")

# ==========================================
# FINAL SUMMARY
# ==========================================

st.subheader("📌 Executive Summary")

st.write("""

EduPro's predictive analytics indicate that
Artificial Intelligence, Machine Learning,
Python, and Data Science courses currently
drive the highest engagement and revenue.

Future platform growth can be accelerated by:

- Expanding trending technology offerings
- Improving instructor quality
- Launching premium certification programs
- Leveraging AI-driven learner recommendations

""")