# ============================================================================
# Slip 01 (PDF Page 3) - Q2 [20 Marks]
# Also appears in: Slip 08 (PDF Page 10) - Q2 [20 Marks], Slip 21 (PDF Page 23) - Q2 (OR) [20 Marks]
#
# QUESTION:
# Q2. Create a suitable dataset named Loan_application.csv containing at
# least 10 records with the
# attributes Application_ID, Age, Income, Credit_Score, Loan_Amount,
# Employment_Years,
# Debt_Ratio, and Loan_Status, where Loan_Status represents whether the
# loan application is
# Approved or Rejected.
# Write a Python program to perform the following data reduction
# techniques:
# a) Feature Selection: Identify the important features for predicting
# Loan_Status.
# b) Feature Extraction: Reduce the number of numerical attributes using a
# suitable technique such
# as Principal Component Analysis (PCA).
#
# [20 Marks]
# ============================================================================

import os
import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

p = "datasets/Loan_application.csv" if os.path.exists("datasets/Loan_application.csv") else "Loan_application.csv"
try:
    df = pd.read_csv(p)
except Exception:
    df = pd.DataFrame({
        "Age": [28, 45, 35, 52, 23, 40, 31, 60, 26, 48],
        "Income": [45000, 85000, 62000, 110000, 28000, 75000, 52000, 95000, 32000, 88000],
        "Credit_Score": [680, 750, 710, 820, 590, 730, 650, 790, 610, 770],
        "Loan_Amount": [150000, 300000, 200000, 450000, 80000, 250000, 180000, 350000, 100000, 320000],
        "Employment_Years": [3, 15, 8, 22, 1, 12, 5, 28, 2, 18],
        "Debt_Ratio": [0.25, 0.18, 0.32, 0.15, 0.45, 0.22, 0.38, 0.12, 0.42, 0.20],
        "Loan_Status": [1, 1, 1, 1, 0, 1, 0, 1, 0, 1]
    })

feature_cols = ["Age", "Income", "Credit_Score", "Loan_Amount", "Employment_Years", "Debt_Ratio"]
X = df[feature_cols]
y = df["Loan_Status"].map({"Approved": 1, "Rejected": 0}) if df["Loan_Status"].dtype == "object" else df["Loan_Status"]

selector = SelectKBest(score_func=f_classif, k=3).fit(X, y)
print("Selected Top Features:", [feature_cols[i] for i in selector.get_support(indices=True)])

X_scaled = StandardScaler().fit_transform(X)
pca = PCA(n_components=2).fit_transform(X_scaled)
print("\nPCA Reduced Components (2D):\n", pd.DataFrame(pca, columns=["PC1", "PC2"]))
