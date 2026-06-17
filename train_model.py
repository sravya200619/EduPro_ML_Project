import pandas as pd
import joblib
import numpy as np
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# =====================================================
# CREATE FOLDERS
# =====================================================

os.makedirs("model", exist_ok=True)
os.makedirs("data", exist_ok=True)

# =====================================================
# LOAD DATA
# =====================================================

data = pd.read_csv("data/merged_data.csv")

print("✅ Dataset Loaded Successfully!")

print("\nColumns Found:")
print(data.columns.tolist())

# =====================================================
# HANDLE MISSING VALUES
# =====================================================

data = data.dropna()

# =====================================================
# LABEL ENCODING
# =====================================================

category_encoder = LabelEncoder()
type_encoder = LabelEncoder()
level_encoder = LabelEncoder()

data["CourseCategory"] = category_encoder.fit_transform(
    data["CourseCategory"]
)

data["CourseType"] = type_encoder.fit_transform(
    data["CourseType"]
)

data["CourseLevel"] = level_encoder.fit_transform(
    data["CourseLevel"]
)

# =====================================================
# SAVE ENCODERS
# =====================================================

joblib.dump(
    category_encoder,
    "model/category_encoder.pkl"
)

joblib.dump(
    type_encoder,
    "model/type_encoder.pkl"
)

joblib.dump(
    level_encoder,
    "model/level_encoder.pkl"
)

print("✅ Encoders Saved!")

# =====================================================
# FEATURE ENGINEERING
# =====================================================

# PriceBand

if "CoursePrice" in data.columns:

    data["PriceBand"] = pd.cut(

        data["CoursePrice"],

        bins=[0, 1000, 5000, 100000],

        labels=[0, 1, 2]

    ).astype(int)

else:

    data["PriceBand"] = 0

# ExperienceLevel

data["ExperienceLevel"] = pd.cut(

    data["YearsOfExperience"],

    bins=[0, 3, 7, 50],

    labels=[0, 1, 2],

    include_lowest=True

).astype(int)

# RatingTier

data["RatingTier"] = pd.cut(

    data["CourseRating"],

    bins=[0, 3.5, 4.5, 5],

    labels=[0, 1, 2],

    include_lowest=True

).astype(int)

print("✅ Feature Engineering Completed!")

# =====================================================
# FEATURES
# =====================================================

features = [

    "CourseCategory",
    "CourseType",
    "CourseLevel",
    "CourseDuration",
    "CourseRating",
    "TeacherRating",
    "YearsOfExperience",
    "PriceBand",
    "ExperienceLevel",
    "RatingTier"

]

# =====================================================
# TARGET
# =====================================================

target = "EnrollmentCount"

X = data[features]
y = data[target]

# =====================================================
# TRAIN TEST SPLIT
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,
    test_size=0.2,
    random_state=42

)

print("✅ Train-Test Split Done!")

# =====================================================
# RANDOM FOREST MODEL
# =====================================================

rf_model = RandomForestRegressor(

    n_estimators=300,
    max_depth=12,
    min_samples_split=5,
    random_state=42,
    n_jobs=-1

)

print("✅ Training Random Forest Model...")

rf_model.fit(
    X_train,
    y_train
)

# =====================================================
# PREDICTIONS
# =====================================================

predictions = rf_model.predict(
    X_test
)

# =====================================================
# EVALUATION
# =====================================================

mae = mean_absolute_error(
    y_test,
    predictions
)

rmse = np.sqrt(
    mean_squared_error(
        y_test,
        predictions
    )
)

r2 = r2_score(
    y_test,
    predictions
)

print("\n==============================")
print("📊 MODEL PERFORMANCE")
print("==============================")

print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.4f}")

# =====================================================
# SAVE MODEL
# =====================================================

joblib.dump(

    rf_model,
    "model/best_model.pkl"

)

print("\n✅ Model Saved Successfully!")

# =====================================================
# FEATURE IMPORTANCE
# =====================================================

importance_df = pd.DataFrame({

    "Feature": features,

    "Importance": rf_model.feature_importances_

})

importance_df = importance_df.sort_values(

    by="Importance",
    ascending=False

)

print("\n📌 Feature Importance")

print(importance_df)

# =====================================================
# SAVE FEATURE IMPORTANCE
# =====================================================

importance_df.to_csv(

    "data/feature_importance.csv",
    index=False

)

print("✅ Feature Importance Saved!")

# =====================================================
# SAVE MODEL RESULTS
# =====================================================

results_df = pd.DataFrame({

    "Model": ["Random Forest"],

    "MAE": [mae],

    "RMSE": [rmse],

    "R2": [r2]

})

results_df.to_csv(

    "data/model_results.csv",
    index=False

)

print("✅ Model Results Saved!")

# =====================================================
# SAVE TRAINING FEATURES
# =====================================================

joblib.dump(

    features,
    "model/features.pkl"

)

print("✅ Feature List Saved!")

print("\n🎉 Training Completed Successfully!")