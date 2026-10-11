# ============================================================================
# Slip 01 (PDF Page 3) - Q2 (OR) [20 Marks]
#
# QUESTION:
# Q2. Using the built-in Iris dataset, apply K-Means clustering with K =
# 3. Plot the datapoints, visualize
# the clusters with different colors, and display the cluster centroids.
# [20 Marks]
# ============================================================================

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

iris = load_iris()
X = iris.data[:, :2]

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10).fit(X)

plt.figure(figsize=(7, 4))
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap="viridis", s=50)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c="red", marker="X", s=200, label="Centroids")
plt.title("K-Means on Iris (K = 3)")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.legend()
plt.show()
print("Centroids:\n", kmeans.cluster_centers_)
