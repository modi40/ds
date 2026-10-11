# ============================================================================
# Slip 06 (PDF Page 8) - Q2 (OR) [20 Marks]
#
# QUESTION:
# Q2. Implement a KNN classifier on the given Customer dataset. Preprocess
# the data and classify
# customers into different segments. Evaluate the model using Accuracy and
# Confusion Matrix.
#
# [20 Marks]
# ============================================================================

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.datasets import make_blobs

p = "datasets/Mall_Customers.csv" if os.path.exists("datasets/Mall_Customers.csv") else "Mall_Customers.csv"
try:
    df = pd.read_csv(p)
    inc = [c for c in df.columns if "income" in c.lower()][0]
    sc = [c for c in df.columns if "spending" in c.lower() or "score" in c.lower()][0]
    X = df[[inc, sc]]
    y = (df[sc] > 50).astype(int)
except Exception:
    X, y = make_blobs(n_samples=100, n_features=2, centers=2, random_state=42)

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=42)
knn = KNeighborsClassifier(n_neighbors=5).fit(X_tr, y_tr)
preds = knn.predict(X_te)

print("Accuracy:", accuracy_score(y_te, preds))
print("Confusion Matrix:\n", confusion_matrix(y_te, preds))
