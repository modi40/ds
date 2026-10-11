# ============================================================================
# Slip 12 (PDF Page 14) - Q2 [20 Marks]
#
# QUESTION:
# Q2. Apply Polynomial Regression to predict song popularity using audio
# features such as
# danceability, energy, and tempo. Evaluate the model using MAE, RMSE, and
# R² Score, and
# visualize the fitted curve.
#
# [20 Marks]
# ============================================================================

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

p = "datasets/Spotify_Raw_Data.csv" if os.path.exists("datasets/Spotify_Raw_Data.csv") else "Spotify_Raw_Data.csv"
try:
    df = pd.read_csv(p)
    X, y = df[["danceability", "energy", "tempo"]], df["popularity"]
except Exception:
    X = pd.DataFrame({"danceability": [0.3, 0.5, 0.7, 0.9], "energy": [0.4, 0.6, 0.8, 0.95], "tempo": [90, 110, 130, 150]})
    y = pd.Series([30, 55, 75, 95])

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

X_tr, X_te, y_tr, y_te = train_test_split(X_poly, y, test_size=0.25, random_state=42)
model = LinearRegression().fit(X_tr, y_tr)
preds = model.predict(X_te)

print("MAE :", mean_absolute_error(y_te, preds))
print("RMSE:", np.sqrt(mean_squared_error(y_te, preds)))
print("R2  :", r2_score(y_te, preds))

plt.figure(figsize=(7, 4))
p1d = PolynomialFeatures(degree=2)
x_plot = df[["danceability"]].sort_values("danceability")
m1d = LinearRegression().fit(p1d.fit_transform(df[["danceability"]]), y)
plt.scatter(df["danceability"], y, color="blue")
plt.plot(x_plot["danceability"], m1d.predict(p1d.fit_transform(x_plot)), color="red")
plt.title("Polynomial Regression: Song Popularity")
plt.xlabel("Danceability")
plt.ylabel("Popularity")
plt.show()
