# ============================================================================
# Slip 14 (PDF Page 16) - Q2 [20 Marks]
# Also appears in: Slip 24 (PDF Page 26) - Q2 (OR) [20 Marks]
#
# QUESTION:
# Q2. Using the Car Price Prediction dataset, apply Polynomial Regression
# to predict the Selling Price
# based on Vehicle Age, Present Price, and Kilometers Driven. Evaluate the
# model using the R²
# Score and visualize the actual data points along with the fitted
# polynomial curve.
#
# [20 Marks]
# ============================================================================

import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

p = "datasets/car_data.csv" if os.path.exists("datasets/car_data.csv") else "car_data.csv"
try:
    df = pd.read_csv(p)
    X, y = df[["Vehicle_Age", "Present_Price", "Kms_Driven"]], df["Selling_Price"]
except Exception:
    X = pd.DataFrame({"Vehicle_Age": [2, 4, 6, 8, 10], "Present_Price": [6.0, 9.0, 12.0, 8.0, 7.0], "Kms_Driven": [15000, 35000, 60000, 75000, 95000]})
    y = pd.Series([5.0, 7.2, 8.5, 4.0, 3.0])

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

X_tr, X_te, y_tr, y_te = train_test_split(X_poly, y, test_size=0.25, random_state=42)
model = LinearRegression().fit(X_tr, y_tr)
preds = model.predict(X_te)

print("R2 Score:", r2_score(y_te, preds))

plt.figure(figsize=(7, 4))
p1d = PolynomialFeatures(degree=2)
x_plot = df[["Present_Price"]].sort_values("Present_Price")
m1d = LinearRegression().fit(p1d.fit_transform(df[["Present_Price"]]), y)
plt.scatter(df["Present_Price"], y, color="darkgreen")
plt.plot(x_plot["Present_Price"], m1d.predict(p1d.fit_transform(x_plot)), color="red")
plt.title("Car Price Prediction: Polynomial Curve")
plt.xlabel("Present Price")
plt.ylabel("Selling Price")
plt.show()
