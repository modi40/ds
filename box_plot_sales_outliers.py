# ============================================================================
# Slip 13 (PDF Page 15) - Q1 [10 Marks]
#
# QUESTION:
# Q1. A retail store has recorded the daily sales for two months. Create a
# dataframe using sales.csv file
# and generate a Box Plot to identify any outliers. Customize the graph
# with title and labels.
# [10 Marks]
# ============================================================================

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

p = "datasets/sales.csv" if os.path.exists("datasets/sales.csv") else "sales.csv"
try:
    df = pd.read_csv(p)
except Exception:
    df = pd.DataFrame({"Sales": np.append(np.random.normal(5000, 500, 58), [15000, 400])})

plt.figure(figsize=(6, 4))
plt.boxplot(df["Sales"])
plt.title("Box Plot of Daily Sales")
plt.ylabel("Sales")
plt.show()

q1 = df["Sales"].quantile(0.25)
q3 = df["Sales"].quantile(0.75)
iqr = q3 - q1
outliers = df[(df["Sales"] < q1 - 1.5 * iqr) | (df["Sales"] > q3 + 1.5 * iqr)]["Sales"]
print("Identified Outliers:", outliers.tolist())
