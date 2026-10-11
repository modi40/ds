# ============================================================================
# Slip 03 (PDF Page 5) - Q2 (OR) [20 Marks]
# Also appears in: Slip 19 (PDF Page 21) - Q2 (OR) [20 Marks]
#
# QUESTION:
# Q2. Apply the Random Forest algorithm on the Heart Disease dataset to
# predict the presence of heart
# disease. Preprocess the data, evaluate the model using accuracy and
# confusion matrix.
#
# [20 Marks]
# ============================================================================

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.datasets import make_classification

p = "datasets/heart.csv" if os.path.exists("datasets/heart.csv") else "heart.csv"
try:
    df = pd.read_csv(p)
    X, y = df.drop(columns=["target"]), df["target"]
except Exception:
    X, y = make_classification(n_samples=100, n_features=6, random_state=42)

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=42)
rf = RandomForestClassifier(n_estimators=50, random_state=42).fit(X_tr, y_tr)
preds = rf.predict(X_te)

print("Accuracy :", accuracy_score(y_te, preds))
print("Precision:", precision_score(y_te, preds, average="weighted"))
print("Recall   :", recall_score(y_te, preds, average="weighted"))
print("F1-Score :", f1_score(y_te, preds, average="weighted"))
print("Confusion Matrix:\n", confusion_matrix(y_te, preds))
