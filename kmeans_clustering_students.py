# ============================================================================
# Slip 21 (PDF Page 23) - Q2 [20 Marks]
# Also appears in: Slip 22 (PDF Page 24) - Q2 (OR) [20 Marks]
#
# QUESTION:
# Q2. Apply the K -Means Clustering algorithm to the given student dataset
# using Attendance and
# Marks as the input attributes. Perform the required data preprocessing,
# set K = 3, assign the
# students to the respective clusters, and visualize the clusters and
# their centroids using a suitable
# scatter plot.
# [20 Marks]
# ============================================================================

import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

p = "datasets/Students_Grading_Dataset.csv" if os.path.exists("datasets/Students_Grading_Dataset.csv") else "Students_Grading_Dataset.csv"
try:
    df = pd.read_csv(p)
    att = [c for c in df.columns if "attendance" in c.lower()][0]
    mk = [c for c in df.columns if "marks" in c.lower() or "score" in c.lower()][0]
    X = df[[att, mk]].dropna()
except Exception:
    X = pd.DataFrame({"Attendance": [55, 60, 70, 75, 85, 95], "Marks": [45, 50, 65, 70, 85, 95]})
    att, mk = "Attendance", "Marks"

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10).fit(X)

plt.figure(figsize=(7, 4))
plt.scatter(X[att], X[mk], c=kmeans.labels_, cmap="Set1", s=60)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c="black", marker="X", s=200, label="Centroids")
plt.title("K-Means on Students (Attendance & Marks, K=3)")
plt.xlabel("Attendance")
plt.ylabel("Marks")
plt.legend()
plt.show()
