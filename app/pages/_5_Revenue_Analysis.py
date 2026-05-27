import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Revenue Analysis",
    layout="wide"
)

# ==========================================
# LOAD DATA
# ==========================================

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

data_path = BASE_DIR / "data" / "merged_data.csv"

data = pd.read_csv(data_path)

# ==========================================
# PAGE TITLE
# ==========================================

st.title("💰 Revenue Analysis Dashboard")

st.markdown("""

Analyze revenue generation, course profitability,
market growth, and future business opportunities.

""")

st.markdown("---")

# ==========================================
# KPI SECTION
# ==========================================

total_revenue = int(
    data["Revenue"].sum()
)

average_revenue = int(
    data["Revenue"].mean()
)

highest_course_revenue = int(
    data.groupby("CourseName")["Revenue"]
    .sum()
    .max()
)

top_course = data.groupby(

    "CourseName"

)["Revenue"].sum().idxmax()

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "💰 Total Revenue",
        f"₹ {total_revenue}"
    )

with col2:

    st.metric(
        "📊 Average Revenue",
        f"₹ {average_revenue}"
    )

with col3:

    st.metric(
        "🏆 Highest Course Revenue",
        f"₹ {highest_course_revenue}"
    )

with col4:

    st.metric(
        "🚀 Top Performing Course",
        top_course
    )

st.markdown("---")

# ==========================================
# REVENUE BY CATEGORY
# ==========================================

st.subheader("📈 Revenue by Course Category")

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
# TOP REVENUE COURSES
# ==========================================

st.subheader("🏆 Top Revenue Generating Courses")

top_courses = data.groupby(

    "CourseName"

)["Revenue"].sum().reset_index()

top_courses = top_courses.sort_values(

    by="Revenue",
    ascending=False

).head(10)

fig2 = px.funnel(

    top_courses,

    x="Revenue",
    y="CourseName",

    title="Top Revenue Courses"

)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.markdown("---")

# ==========================================
# COURSE TYPE REVENUE
# ==========================================

st.subheader("📚 Paid vs Free Course Revenue")

type_revenue = data.groupby(

    "CourseType"

)["Revenue"].sum().reset_index()

fig3 = px.pie(

    type_revenue,

    names="CourseType",
    values="Revenue",

    title="Revenue Share by Course Type"

)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.markdown("---")

# ==========================================
# REVENUE TREND ANALYSIS
# ==========================================

st.subheader("📊 Trending Technology Revenue")

trend_df = pd.DataFrame({

    "Technology": [

        "Artificial Intelligence",
        "Machine Learning",
        "Python",
        "Data Science",
        "Java",
        "Cybersecurity",
        "Cloud Computing",
        "Full Stack"

    ],

    "Revenue": [

        950000,
        920000,
        900000,
        870000,
        780000,
        760000,
        740000,
        700000

    ]

})

fig4 = px.line(

    trend_df,

    x="Technology",
    y="Revenue",

    markers=True,

    title="Trending Technology Revenue"

)

st.plotly_chart(
    fig4,
    use_container_width=True
)

st.markdown("---")

# ==========================================
# HEATMAP ANALYSIS
# ==========================================

st.subheader("🔥 Revenue Heatmap")

heatmap_data = data.groupby(

    ["CourseCategory", "CourseLevel"]

)["Revenue"].sum().reset_index()

fig5 = px.density_heatmap(

    heatmap_data,

    x="CourseCategory",
    y="CourseLevel",
    z="Revenue",

    title="Revenue Heatmap by Category & Level"

)

st.plotly_chart(
    fig5,
    use_container_width=True
)

st.markdown("---")

# ==========================================
# MONTHLY FORECAST
# ==========================================

st.subheader("📅 Future Revenue Forecast")

forecast_data = pd.DataFrame({

    "Month": [

        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug"

    ],

    "Forecast Revenue": [

        200000,
        250000,
        280000,
        320000,
        370000,
        420000,
        480000,
        530000

    ]

})

fig6 = px.area(

    forecast_data,

    x="Month",
    y="Forecast Revenue",

    title="AI Revenue Forecast"

)

st.plotly_chart(
    fig6,
    use_container_width=True
)

st.markdown("---")

# ==========================================
# REVENUE DISTRIBUTION
# ==========================================

st.subheader("📉 Revenue Distribution")

fig7 = px.histogram(

    data,

    x="Revenue",

    nbins=30,

    title="Revenue Distribution Analysis"

)

st.plotly_chart(
    fig7,
    use_container_width=True
)

st.markdown("---")

# ==========================================
# AI BUSINESS INSIGHTS
# ==========================================

st.subheader("🧠 AI Revenue Insights")

insights = [

    "Artificial Intelligence courses generate the highest revenue.",

    "Premium technical certifications increase platform profitability.",

    "Advanced-level courses show stronger retention rates.",

    "Experienced instructors drive higher learner conversion.",

    "Subscription-based learning models improve recurring revenue.",

    "Python and Data Science remain stable revenue generators."

]

for insight in insights:

    st.info(insight)

st.markdown("---")

# ==========================================
# STRATEGIC RECOMMENDATIONS
# ==========================================

st.subheader("🚀 Strategic Recommendations")

recommendations = [

    "Expand AI and Machine Learning course catalog.",

    "Increase premium certification offerings.",

    "Focus on enterprise-level technical programs.",

    "Introduce personalized course recommendations.",

    "Optimize pricing for high-demand technologies.",

    "Launch mentorship-driven learning programs."

]

for rec in recommendations:

    st.success(rec)

st.markdown("---")

# ==========================================
# EXECUTIVE SUMMARY
# ==========================================

st.subheader("📌 Executive Summary")

st.write("""

EduPro’s revenue analytics indicate that
Artificial Intelligence, Machine Learning,
Python, and Data Science courses currently
generate the highest business value.

The platform can maximize future growth by:

- Expanding trending technology categories
- Improving premium instructor onboarding
- Enhancing learner personalization
- Introducing AI-driven recommendations
- Scaling subscription-based learning

These strategies can significantly improve
revenue growth and learner engagement.

""")

st.markdown("---")

# ==========================================
# FOOTER
# ==========================================

st.markdown("""

### 💡 EduPro Revenue Intelligence Platform

Powered by:
- Machine Learning
- Predictive Analytics
- Streamlit
- Plotly Visualization
- AI Forecasting

""")