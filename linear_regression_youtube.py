# ============================================================================
# Slip 02 (PDF Page 4) - Q2 [20 Marks]
#
# QUESTION:
# Q2. Apply Linear Regression on a YouTube Video dataset to predict video
# views using relevant video
# attributes. Visualize the relationship between the predictor and target
# variable using a scatter plot
# and regression line.
#
# [20 Marks]
# ============================================================================

import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

p = "datasets/USvideos.csv" if os.path.exists("datasets/USvideos.csv") else "USvideos.csv"
try:
    df = pd.read_csv(p)
    X, y = df[["likes"]], df["views"]
except Exception:
    X = pd.DataFrame({"likes": [5000, 25000, 80000, 180000, 320000]})
    y = pd.Series([100000, 550000, 1800000, 3800000, 7000000])

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=42)
model = LinearRegression().fit(X_tr, y_tr)
preds = model.predict(X_te)

print("R2 :", r2_score(y_te, preds))
print("MSE:", mean_squared_error(y_te, preds))

plt.figure(figsize=(7, 4))
plt.scatter(X, y, color="purple")
plt.plot(X, model.predict(X), color="orange", label="Regression Line")
plt.title("YouTube Views Prediction")
plt.xlabel("Likes")
plt.ylabel("Views")
plt.legend()
plt.show()
