# ============================================================================
# Slip 20 (PDF Page 22) - Q1 [10 Marks]
#
# QUESTION:
# Q1. Write a Python program to create a DataFrame containing the
# attributes Age, Salary, Experience,
# Working_Hours, and Performance_Score. Apply the Standardization data
# transformation
# technique and display the transformed data.
# [10 Marks]
# ============================================================================

import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.DataFrame({
    "Age": [25, 32, 45, 29, 50],
    "Salary": [35000, 55000, 85000, 42000, 95000],
    "Experience": [2, 6, 18, 4, 22],
    "Working_Hours": [40, 45, 50, 38, 42],
    "Performance_Score": [3.2, 3.8, 4.5, 3.5, 4.8]
})

scaled = StandardScaler().fit_transform(df)
print("Standardized Data:\n", pd.DataFrame(scaled, columns=df.columns))
