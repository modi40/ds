# ============================================================================
# Slip 21 (PDF Page 23) - Q1 [10 Marks]
#
# QUESTION:
# Q1. Create a dataframe using weather.csv containing values of
# Temperature, Humidity, Rainfall, and
# Wind Speed. Generate a Heat Map to visualize the correlation between
# these weather parameters.
# [10 Marks]
# ============================================================================

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

p = "datasets/weather.csv" if os.path.exists("datasets/weather.csv") else "weather.csv"
try:
    df = pd.read_csv(p)
except Exception:
    df = pd.DataFrame({
        "Temperature": [25, 28, 32, 35, 22, 19, 29, 31],
        "Humidity": [80, 75, 60, 45, 85, 90, 70, 65],
        "Rainfall": [12, 8, 2, 0, 18, 25, 5, 1],
        "Wind Speed": [15, 12, 18, 22, 10, 8, 14, 16]
    })

corr = df[["Temperature", "Humidity", "Rainfall", "Wind Speed"]].corr()
print("Correlation Matrix:\n", corr)

plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap="YlGnBu", fmt=".2f")
plt.title("Weather Parameters Correlation Heatmap")
plt.tight_layout()
plt.show()
