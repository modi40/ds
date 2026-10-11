# ============================================================================
# Slip 10 (PDF Page 12) - Q2 [20 Marks]
#
# QUESTION:
# Q2. Using the given housing dataset, develop a Random Forest Regression
# model to predict house
# prices based on the available property attributes. Perform the necessary
# data preprocessing, train
# and test the model, and evaluate its predictive performance using Mean
# Absolute Error (MAE),
# Root Mean Squared Error (RMSE), and R² Score.
# ============================================================================

import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.datasets import fetch_california_housing

p = "datasets/housing.csv" if os.path.exists("datasets/housing.csv") else "housing.csv"
try:
    df = pd.read_csv(p).dropna()
    num_df = df.select_dtypes(include=[np.number])
    tgt = [c for c in num_df.columns if "value" in c.lower() or "price" in c.lower()][-1]
    X, y = num_df.drop(columns=[tgt]), num_df[tgt]
except Exception:
    cal = fetch_california_housing()
    X, y = pd.DataFrame(cal.data, columns=cal.feature_names), cal.target

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
rf = RandomForestRegressor(n_estimators=50, random_state=42).fit(X_tr, y_tr)
preds = rf.predict(X_te)

print("MAE :", mean_absolute_error(y_te, preds))
print("RMSE:", np.sqrt(mean_squared_error(y_te, preds)))
print("R2  :", r2_score(y_te, preds))
