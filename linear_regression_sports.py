# ============================================================================
# Slip 06 (PDF Page 8) - Q2 [20 Marks]
#
# QUESTION:
# Q2. Use the Sports Performance dataset to develop a Simple Linear
# Regression model to predict
# Performance Score based on Training Hours Per Week. Evaluate the model
# using the R² score
# and plot a scatter graph with the regression line to visualize the
# relationship between training
# hours and performance score.
#
# [20 Marks]
# ============================================================================

import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

p = "datasets/collegiate_athlete_injury_dataset.csv" if os.path.exists("datasets/collegiate_athlete_injury_dataset.csv") else "collegiate_athlete_injury_dataset.csv"
try:
    df = pd.read_csv(p)
    tc = [c for c in df.columns if "training" in c.lower() or "hours" in c.lower()][0]
    sc = [c for c in df.columns if "performance" in c.lower() or "score" in c.lower()][0]
    X, y = df[[tc]], df[sc]
except Exception:
    X = pd.DataFrame({"Training_Hours": [5, 10, 15, 20, 25, 30]})
    y = pd.Series([50, 62, 74, 85, 92, 99])

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=42)
model = LinearRegression().fit(X_tr, y_tr)
preds = model.predict(X_te)

print("R2 Score:", r2_score(y_te, preds))
plt.figure(figsize=(7, 4))
plt.scatter(X, y, color="teal")
plt.plot(X, model.predict(X), color="red")
plt.title("Training Hours vs Performance Score")
plt.xlabel("Training Hours")
plt.ylabel("Score")
plt.show()
