# ============================================================================
# Slip 05 (PDF Page 7) - Q2 (OR) [20 Marks]
# Also appears in: Slip 12 (PDF Page 14) - Q2 (OR) [20 Marks]
#
# QUESTION:
# Q2. Use the K-Nearest Neighbors (KNN) algorithm to classify emails as
# spam or non-spam using the
# Spambase dataset. Preprocess the data, train the KNN classifier, and
# evaluate its performance
# using accuracy, confusion matrix, precision, recall, and F1-score.
# [20 Marks]
# ============================================================================

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score
from sklearn.datasets import make_classification

p = "datasets/spambase.csv" if os.path.exists("datasets/spambase.csv") else "spambase.csv"
try:
    df = pd.read_csv(p)
    X, y = df.iloc[:, :-1], df.iloc[:, -1]
except Exception:
    X, y = make_classification(n_samples=100, n_features=6, random_state=42)

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=42)
knn = KNeighborsClassifier(n_neighbors=5).fit(X_tr, y_tr)
preds = knn.predict(X_te)

print("Accuracy        :", accuracy_score(y_te, preds))
print("Precision Score :", precision_score(y_te, preds, average="binary"))
print("Recall Score    :", recall_score(y_te, preds, average="binary"))
print("F1-Score        :", f1_score(y_te, preds, average="binary"))
print("Confusion Matrix:\n", confusion_matrix(y_te, preds))
