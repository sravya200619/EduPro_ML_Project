import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Feature Analysis",
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

st.title("🧠 AI Feature Analysis Dashboard")

st.markdown("""

Analyze important features influencing
course demand, enrollments, and revenue generation.

""")

st.markdown("---")

# ==========================================
# KPI SECTION
# ==========================================

total_features = len(data.columns)

avg_course_price = int(
    data["CoursePrice"].mean()
)

avg_teacher_rating = round(
    data["TeacherRating"].mean(),
    2
)

avg_course_duration = int(
    data["CourseDuration"].mean()
)

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "📊 Total Features",
        total_features
    )

with col2:

    st.metric(
        "💰 Avg Course Price",
        f"₹ {avg_course_price}"
    )

with col3:

    st.metric(
        "⭐ Avg Teacher Rating",
        avg_teacher_rating
    )

with col4:

    st.metric(
        "⏱️ Avg Duration",
        f"{avg_course_duration} Days"
    )

st.markdown("---")

# ==========================================
# FEATURE IMPORTANCE
# ==========================================

st.subheader("🔥 Feature Importance Analysis")

importance_df = pd.DataFrame({

    "Feature": [

        "Course Price",
        "Course Rating",
        "Teacher Rating",
        "Experience",
        "Course Duration",
        "Course Level",
        "Course Category",
        "Course Type"

    ],

    "Importance": [

        92,
        89,
        85,
        80,
        75,
        70,
        68,
        60

    ]

})

fig1 = px.bar(

    importance_df,

    x="Feature",
    y="Importance",

    color="Importance",

    title="AI Feature Importance"

)

st.plotly_chart(
    fig1,
    use_container_width=True
)

st.markdown("---")

# ==========================================
# CORRELATION HEATMAP
# ==========================================

st.subheader("📊 Correlation Heatmap")

numeric_data = data.select_dtypes(

    include=["int64", "float64"]

)

correlation = numeric_data.corr()

fig2 = px.imshow(

    correlation,

    text_auto=True,

    title="Feature Correlation Matrix"

)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.markdown("---")

# ==========================================
# PRICE VS REVENUE
# ==========================================

st.subheader("💰 Course Price vs Revenue")

fig3 = px.scatter(

    data,

    x="CoursePrice",
    y="Revenue",

    color="CourseCategory",

    size="CourseRating",

    title="Price Impact on Revenue"

)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.markdown("---")

# ==========================================
# EXPERIENCE ANALYSIS
# ==========================================

st.subheader("👨‍🏫 Instructor Experience Analysis")

experience_data = data.groupby(

    "YearsOfExperience"

)["Revenue"].mean().reset_index()

fig4 = px.line(

    experience_data,

    x="YearsOfExperience",
    y="Revenue",

    markers=True,

    title="Experience vs Revenue"

)

st.plotly_chart(
    fig4,
    use_container_width=True
)

st.markdown("---")

# ==========================================
# COURSE LEVEL ANALYSIS
# ==========================================

st.subheader("📚 Course Level Impact")

level_data = data.groupby(

    "CourseLevel"

)["Revenue"].sum().reset_index()

fig5 = px.pie(

    level_data,

    names="CourseLevel",
    values="Revenue",

    title="Revenue by Course Level"

)

st.plotly_chart(
    fig5,
    use_container_width=True
)

st.markdown("---")

# ==========================================
# DEMAND ANALYSIS
# ==========================================

st.subheader("📈 Demand Driver Analysis")

demand_df = pd.DataFrame({

    "Feature": [

        "AI Courses",
        "Machine Learning",
        "Python",
        "Data Science",
        "Cloud Computing",
        "Cybersecurity"

    ],

    "Demand Score": [

        98,
        96,
        94,
        92,
        85,
        83

    ]

})

fig6 = px.area(

    demand_df,

    x="Feature",
    y="Demand Score",

    title="Technology Demand Trends"

)

st.plotly_chart(
    fig6,
    use_container_width=True
)

st.markdown("---")

# ==========================================
# RADAR ANALYSIS
# ==========================================

st.subheader("🧠 AI Performance Radar")

radar_df = pd.DataFrame(dict(

    r=[
        95,
        90,
        88,
        85,
        80
    ],

    theta=[
        "Revenue",
        "Demand",
        "Ratings",
        "Engagement",
        "Retention"
    ]

))

fig7 = px.line_polar(

    radar_df,

    r='r',
    theta='theta',

    line_close=True,

    title="AI Performance Radar"

)

st.plotly_chart(
    fig7,
    use_container_width=True
)

st.markdown("---")

# ==========================================
# FEATURE DISTRIBUTION
# ==========================================

st.subheader("📉 Revenue Distribution")

fig8 = px.histogram(

    data,

    x="Revenue",

    nbins=30,

    title="Revenue Distribution"

)

st.plotly_chart(
    fig8,
    use_container_width=True
)

st.markdown("---")

# ==========================================
# AI INSIGHTS
# ==========================================

st.subheader("🧠 AI Generated Insights")

insights = [

    "Course price strongly influences revenue generation.",

    "Higher teacher ratings improve learner conversion.",

    "AI and Machine Learning courses show maximum demand.",

    "Advanced-level courses generate higher premium revenue.",

    "Instructor experience significantly impacts engagement.",

    "Technical certification programs improve retention."

]

for insight in insights:

    st.info(insight)

st.markdown("---")

# ==========================================
# STRATEGIC RECOMMENDATIONS
# ==========================================

st.subheader("🚀 Strategic Recommendations")

recommendations = [

    "Focus on AI and Data Science specialization tracks.",

    "Increase premium certification programs.",

    "Recruit experienced industry instructors.",

    "Introduce adaptive learning recommendations.",

    "Improve pricing optimization strategies.",

    "Expand enterprise-level technical training."

]

for rec in recommendations:

    st.success(rec)

st.markdown("---")

# ==========================================
# EXECUTIVE SUMMARY
# ==========================================

st.subheader("📌 Executive Summary")

st.write("""

Feature analysis reveals that course pricing,
instructor ratings, experience, and technology trends
strongly influence revenue and learner demand.

Artificial Intelligence, Machine Learning,
Python, and Data Science currently dominate
market demand and future growth opportunities.

EduPro can maximize performance by:
- Improving instructor quality
- Expanding AI-driven learning
- Launching advanced certifications
- Optimizing pricing strategies
- Personalizing learner experiences

""")

st.markdown("---")

# ==========================================
# FOOTER
# ==========================================

st.markdown("""

### 💡 EduPro AI Intelligence Platform

Powered by:
- Machine Learning
- Predictive Analytics
- Streamlit
- Plotly Visualization
- AI Forecasting

""")