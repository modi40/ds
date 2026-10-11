# ============================================================================
# Slip 13 (PDF Page 15) - Q2 [20 Marks]
#
# QUESTION:
# Q2. Implement the K-Nearest Neighbors (KNN) algorithm to classify the
# Wine dataset. Perform the
# required data p reprocessing, model training, and testing, and evaluate
# the model performance
# using Accuracy, Precision, Recall, and F1-Score.
# [20 Marks]
# ============================================================================

import os
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

p = "datasets/Wine.csv" if os.path.exists("datasets/Wine.csv") else "Wine.csv"
try:
    df = pd.read_csv(p)
    X, y = df.iloc[:, :-1], df.iloc[:, -1]
except Exception:
    w = load_wine()
    X, y = w.data, w.target

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=42)
knn = KNeighborsClassifier(n_neighbors=5).fit(X_tr, y_tr)
preds = knn.predict(X_te)

print("Accuracy :", accuracy_score(y_te, preds))
print("Precision:", precision_score(y_te, preds, average="weighted"))
print("Recall   :", recall_score(y_te, preds, average="weighted"))
print("F1-Score :", f1_score(y_te, preds, average="weighted"))
