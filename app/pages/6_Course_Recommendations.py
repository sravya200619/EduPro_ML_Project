import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(layout="wide")

# LOAD DATA

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

data_path = BASE_DIR / "data" / "merged_data.csv"

data = pd.read_csv(data_path)

st.title("🎯 AI Smart Course Recommendation System")

st.markdown(
    """
    Discover trending and high-demand courses
    based on market demand, ratings, and enrollments.
    """
)

# TRENDING TECH COURSES

trending_courses = [

    "Machine Learning",
    "Artificial Intelligence",
    "Python",
    "Java",
    "Data Science",
    "Full Stack Development",
    "Cybersecurity",
    "Cloud Computing"

]

# SIDEBAR

st.sidebar.header("📚 Select Your Interest")

selected_interest = st.sidebar.selectbox(

    "Trending Technologies",

    trending_courses

)

# FILTER RELEVANT COURSES

filtered_data = data[
    data["CourseName"].str.contains(
        selected_interest,
        case=False,
        na=False
    )
]

# IF NO MATCHES FOUND

if filtered_data.empty:

    st.warning(
        "No matching courses found. Showing top trending courses."
    )

    filtered_data = data.sort_values(

        by="CourseRating",
        ascending=False

    ).head(20)

# RECOMMENDATION SCORE

filtered_data["RecommendationScore"] = (

    filtered_data["CourseRating"] * 0.4
    +
    filtered_data["TeacherRating"] * 0.3
    +
    filtered_data["EnrollmentCount"] * 0.3

)

# TOP RECOMMENDED COURSES

top_courses = filtered_data.groupby(

    "CourseName"

).agg({

    "RecommendationScore": "mean",
    "Revenue": "sum",
    "CourseRating": "mean"

}).reset_index()

top_courses = top_courses.sort_values(

    by="RecommendationScore",
    ascending=False

).head(10)

# DISPLAY COURSES

st.subheader("🏆 Recommended Trending Courses")

st.dataframe(
    top_courses
)

# BAR CHART

fig1 = px.bar(

    top_courses,

    x="CourseName",
    y="RecommendationScore",

    color="Revenue",

    title="Top AI Recommended Courses"

)

st.plotly_chart(

    fig1,
    use_container_width=True

)

# HIGH DEMAND COURSES

high_demand = filtered_data.groupby(

    "CourseName"

)["EnrollmentCount"].sum().reset_index()

high_demand = high_demand.sort_values(

    by="EnrollmentCount",
    ascending=False

).head(5)

st.subheader("🔥 High Demand Courses")

fig2 = px.pie(

    high_demand,

    names="CourseName",
    values="EnrollmentCount",

    title="Most Enrolled Trending Courses"

)

st.plotly_chart(

    fig2,
    use_container_width=True

)

# TOP RATED COURSES

top_rated = filtered_data.groupby(

    "CourseName"

)["CourseRating"].mean().reset_index()

top_rated = top_rated.sort_values(

    by="CourseRating",
    ascending=False

).head(5)

st.subheader("⭐ Top Rated Courses")

fig3 = px.scatter(

    top_rated,

    x="CourseName",
    y="CourseRating",

    size="CourseRating",

    title="Top Rated Trending Courses"

)

st.plotly_chart(

    fig3,
    use_container_width=True

)

st.success(
    "AI Recommendation System Loaded Successfully!"
)
# ==========================================
# LEARNING RESOURCES
# ==========================================

resources = {

    "Machine Learning": {

        "Courses": [
            "Andrew Ng Machine Learning",
            "FastAI Practical Deep Learning",
            "Google ML Crash Course"
        ],

        "Skills": [
            "Python",
            "Pandas",
            "Scikit-learn",
            "TensorFlow"
        ],

        "Careers": [
            "ML Engineer",
            "Data Scientist",
            "AI Engineer"
        ],

        "Salary": "₹12 - 25 LPA",

        "Roadmap":
        "Python → Statistics → Machine Learning → Deep Learning"

    },

    "Artificial Intelligence": {

        "Courses": [
            "AI For Everyone",
            "Deep Learning Specialization",
            "Generative AI Fundamentals"
        ],

        "Skills": [
            "Python",
            "Neural Networks",
            "Deep Learning",
            "LLMs"
        ],

        "Careers": [
            "AI Engineer",
            "Research Engineer",
            "Prompt Engineer"
        ],

        "Salary": "₹15 - 30 LPA",

        "Roadmap":
        "Python → ML → Deep Learning → Generative AI"

    },

    "Python": {

        "Courses": [
            "Python for Everybody",
            "Automate the Boring Stuff",
            "Python Bootcamp"
        ],

        "Skills": [
            "Python",
            "OOP",
            "APIs",
            "Automation"
        ],

        "Careers": [
            "Python Developer",
            "Backend Developer",
            "Automation Engineer"
        ],

        "Salary": "₹6 - 15 LPA",

        "Roadmap":
        "Python Basics → Projects → Web Development → AI"

    },

    "Data Science": {

        "Courses": [
            "IBM Data Science",
            "Data Science Bootcamp",
            "Kaggle Micro Courses"
        ],

        "Skills": [
            "Python",
            "SQL",
            "Visualization",
            "Machine Learning"
        ],

        "Careers": [
            "Data Scientist",
            "Data Analyst",
            "Business Analyst"
        ],

        "Salary": "₹10 - 22 LPA",

        "Roadmap":
        "Python → SQL → Statistics → ML → Projects"

    }

}

# ==========================================
# DISPLAY RESOURCES
# ==========================================

if selected_interest in resources:

    st.subheader("📚 Learning Resources")

    st.write(
        resources[selected_interest]["Courses"]
    )

    st.subheader("🛠️ Skills Required")

    st.write(
        resources[selected_interest]["Skills"]
    )

    st.subheader("💼 Career Opportunities")

    st.write(
        resources[selected_interest]["Careers"]
    )

    st.subheader("💰 Average Salary")

    st.success(
        resources[selected_interest]["Salary"]
    )

    st.subheader("🗺️ Learning Roadmap")

    st.info(
        resources[selected_interest]["Roadmap"]
    )