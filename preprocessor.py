import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# ======================================
# LOAD DATA
# ======================================

data = pd.read_csv("data/merged_data.csv")

print("Dataset Loaded Successfully!")

# ======================================
# LABEL ENCODING
# ======================================

encoder = LabelEncoder()

categorical_columns = [
    "CourseCategory",
    "CourseType",
    "CourseLevel",
    "PriceBand",
    "ExperienceLevel",
    "RatingTier"
]

for column in categorical_columns:
    data[column] = encoder.fit_transform(data[column])

print("Categorical Encoding Completed!")

# ======================================
# SELECT FEATURES
# ======================================

X = data[
    [
        "CourseCategory",
        "CourseType",
        "CourseLevel",
        "CoursePrice",
        "CourseDuration",
        "CourseRating",
        "TeacherRating",
        "YearsOfExperience",
        "PriceBand",
        "ExperienceLevel",
        "RatingTier"
    ]
]

# Target Variable
y = data["EnrollmentCount"]

# ======================================
# SPLIT DATA
# ======================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Train Test Split Completed!")

# ======================================
# TRAIN MODEL
# ======================================

model = LinearRegression()

model.fit(X_train, y_train)

print("Model Training Completed!")

# ======================================
# PREDICTIONS
# ======================================

predictions = model.predict(X_test)