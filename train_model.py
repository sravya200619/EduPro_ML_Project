import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
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
# FEATURE SCALING
# ======================================

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("Feature Scaling Completed!")

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

print("Predictions Generated!")

# ======================================
# MODEL EVALUATION
# ======================================

mae = mean_absolute_error(y_test, predictions)

rmse = mean_squared_error(
    y_test,
    predictions
) ** 0.5

r2 = r2_score(y_test, predictions)

print("\nMODEL PERFORMANCE")
print("MAE :", mae)
print("RMSE :", rmse)
print("R2 Score :", r2)

# ======================================
# SAVE MODEL
# ======================================

joblib.dump(
    model,
    "models/forecast_model.pkl"
)

print("\nModel Saved Successfully!")