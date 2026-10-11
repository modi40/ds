# ============================================================================
# Slip 03 (PDF Page 5) - Q2 [20 Marks]
# Also appears in: Slip 08 (PDF Page 10) - Q2 (OR) [20 Marks]
#
# QUESTION:
# Q2. Consider the Salary Dataset. Write a Python program to read the
# dataset and display its
# information. Preprocess the data if required and split it into training
# and testing sets. Apply
# Simple Linear Regression to predict salary based on years of experience.
# Plot the regression line
# and evaluate the model using appropriate metrics such as Mean Squared
# Error.
# [20 Marks]
# ============================================================================

import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

p = "datasets/Salary_Data.csv" if os.path.exists("datasets/Salary_Data.csv") else "Salary_Data.csv"
try:
    df = pd.read_csv(p)
except Exception:
    df = pd.DataFrame({"YearsExperience": [1.1, 2.0, 3.0, 4.0, 5.0, 6.0], "Salary": [39000, 45000, 58000, 62000, 70000, 85000]})

print("Dataset Info:\n", df.head())
X, y = df[["YearsExperience"]], df["Salary"]
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=42)

model = LinearRegression().fit(X_tr, y_tr)
preds = model.predict(X_te)

print("MSE:", mean_squared_error(y_te, preds))
print("R2 :", r2_score(y_te, preds))

plt.figure(figsize=(7, 4))
plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X, model.predict(X), color="red", label="Regression Line")
plt.title("Salary vs Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.legend()
plt.show()
