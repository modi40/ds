# ============================================================================
# Slip 04 (PDF Page 6) - Q2 (OR) [20 Marks]
# Also appears in: Slip 11 (PDF Page 13) - Q2 (OR) [20 Marks]
#
# QUESTION:
# Q2. Apply the K-Means Clustering algorithm on the given E-commerce
# Customer dataset. Read the
# dataset using Python, inspect and preprocess the data by handling
# missing values and selecting
# suitable numerical features. Apply K -Means clustering to segment the
# customers into different
# categories and interpret the resulting clusters.
# [20 Marks]
# ============================================================================

import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

p = "datasets/Mall_Customers.csv" if os.path.exists("datasets/Mall_Customers.csv") else "Mall_Customers.csv"
try:
    df = pd.read_csv(p)
    inc = [c for c in df.columns if "income" in c.lower()][0]
    sc = [c for c in df.columns if "spending" in c.lower() or "score" in c.lower()][0]
    X = df[[inc, sc]].dropna()
except Exception:
    X = pd.DataFrame({"Annual_Income": [15, 16, 60, 65, 90, 95], "Spending_Score": [39, 81, 48, 55, 15, 88]})
    inc, sc = "Annual_Income", "Spending_Score"

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10).fit(X)

plt.figure(figsize=(7, 4))
plt.scatter(X[inc], X[sc], c=kmeans.labels_, cmap="rainbow", s=60)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c="black", marker="X", s=150)
plt.title("Customer Segmentation (K-Means)")
plt.xlabel("Income")
plt.ylabel("Spending Score")
plt.show()
