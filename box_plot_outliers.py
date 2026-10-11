# ============================================================================
# Slip 03 (PDF Page 5) - Q1 [10 Marks]
# Also appears in: Slip 19 (PDF Page 21) - Q1 [10 Marks]
#
# QUESTION:
# Q1. Create a dataframe containing information about different vehicles
# such as Fuel_Efficiency,
# Engine_Power, Vehicle_Weight, Engine_Size, and Acceleration. Add 5
# records in dataframe,
# including outlier. Create Box Plots for Fuel Efficiency and Engine Power
# and identify outliers.
#
# [10 Marks]
# ============================================================================

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Fuel_Efficiency": [18.5, 20.2, 19.0, 48.0, 17.8, 21.0, 16.5],
    "Engine_Power": [110, 125, 115, 130, 420, 105, 140],
    "Vehicle_Weight": [1100, 1150, 1120, 1180, 2500, 1080, 1250],
    "Engine_Size": [1.5, 1.6, 1.5, 1.6, 4.0, 1.4, 1.8],
    "Acceleration": [9.5, 9.1, 9.4, 8.8, 4.2, 10.1, 8.5]
})

plt.figure(figsize=(8, 4))
df[["Fuel_Efficiency", "Engine_Power"]].boxplot()
plt.title("Box Plots for Fuel Efficiency and Engine Power")
plt.show()

for col in ["Fuel_Efficiency", "Engine_Power"]:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    outliers = df[(df[col] < q1 - 1.5 * iqr) | (df[col] > q3 + 1.5 * iqr)][col]
    print(f"Outliers in {col}:", outliers.tolist())
