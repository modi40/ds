# ============================================================================
# Slip 18 (PDF Page 20) - Q1 [10 Marks]
#
# QUESTION:
# Q1. Write a Python program to create an employee_d ata DataFrame with
# the attributes: Emp_ID,
# Age, Dept, Years_Experience, and Performance_Rating. Perform data
# cleaning by handling
# missing values, remove duplicate records and detecting outliers using
# the IQR method.
# [10 Marks]
# ============================================================================

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Emp_ID": [101, 102, 103, 104, 105, 105],
    "Age": [25, np.nan, 35, 75, 28, 28],
    "Dept": ["IT", "HR", np.nan, "IT", "Sales", "Sales"],
    "Years_Experience": [2, 5, 10, 40, 3, 3],
    "Performance_Rating": [4.2, 3.8, np.nan, 5.0, 3.9, 3.9]
})

df = df.drop_duplicates()
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Dept"] = df["Dept"].fillna(df["Dept"].mode()[0])
df["Performance_Rating"] = df["Performance_Rating"].fillna(df["Performance_Rating"].mean())

q1 = df["Age"].quantile(0.25)
q3 = df["Age"].quantile(0.75)
iqr = q3 - q1
df_clean = df[(df["Age"] >= q1 - 1.5 * iqr) & (df["Age"] <= q3 + 1.5 * iqr)]
print("Cleaned DataFrame (Duplicates, Missing & Outliers Handled):\n", df_clean)
