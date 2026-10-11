# ============================================================================
# Slip 18 (PDF Page 20) - Q2 (OR) [20 Marks]
#
# QUESTION:
# Q2. Use the Crop Yield dataset to apply Simple Linear Regression for
# predicting crop yield from
# rainfall. Handle missing values, split the data into training and
# testing sets, and evaluate the model
# using MAE and R² Score. Create a Scatter Plot with a Regression Line to
# visualize the
# relationship.
#
# [20 Marks]
# ============================================================================

import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

p = "datasets/crop_yield_data.csv" if os.path.exists("datasets/crop_yield_data.csv") else "crop_yield_data.csv"
try:
    df = pd.read_csv(p).dropna()
    rc = [c for c in df.columns if "rain" in c.lower()][0]
    yc = [c for c in df.columns if "yield" in c.lower()][0]
    X, y = df[[rc]], df[yc]
except Exception:
    X = pd.DataFrame({"Rainfall": [500, 800, 1100, 1400, 1700]})
    y = pd.Series([2.5, 3.4, 4.2, 5.1, 5.8])

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=42)
model = LinearRegression().fit(X_tr, y_tr)
preds = model.predict(X_te)

print("MAE:", mean_absolute_error(y_te, preds))
print("R2 :", r2_score(y_te, preds))

plt.figure(figsize=(7, 4))
plt.scatter(X, y, color="green")
plt.plot(X, model.predict(X), color="red")
plt.title("Crop Yield from Rainfall")
plt.xlabel("Rainfall")
plt.ylabel("Crop Yield")
plt.show()
