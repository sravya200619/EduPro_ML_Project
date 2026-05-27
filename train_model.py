import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# =====================================================
# LOAD DATA
# =====================================================

data = pd.read_csv("data/merged_data.csv")

print("✅ Dataset Loaded Successfully!")

# =====================================================
# FEATURES
# =====================================================

features = [

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

# =====================================================
# TARGETS
# =====================================================

X = data[features]

y_enrollment = data["EnrollmentCount"]

y_revenue = data["Revenue"]

# =====================================================
# TRAIN TEST SPLIT
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y_enrollment,

    test_size=0.2,
    random_state=42

)

# =====================================================
# RANDOM FOREST MODEL
# =====================================================

model = RandomForestRegressor(

    n_estimators=100,
    random_state=42

)

model.fit(X_train, y_train)

# =====================================================
# PREDICTIONS
# =====================================================

predictions = model.predict(X_test)

# =====================================================
# EVALUATION
# =====================================================

mae = mean_absolute_error(y_test, predictions)

r2 = r2_score(y_test, predictions)

print(f"✅ MAE: {mae}")

print(f"✅ R2 Score: {r2}")

# =====================================================
# SAVE MODEL
# =====================================================

joblib.dump(model, "model/random_forest_model.pkl")

print("✅ Model Saved Successfully!")

# =====================================================
# FEATURE IMPORTANCE
# =====================================================

importance_df = pd.DataFrame({

    "Feature": features,

    "Importance": model.feature_importances_

})

importance_df = importance_df.sort_values(

    by="Importance",
    ascending=False

)

importance_df.to_csv(

    "data/feature_importance.csv",
    index=False

)

print("✅ Feature Importance Saved!")