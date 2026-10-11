# ============================================================================
# Slip 09 (PDF Page 11) - Q2 [20 Marks]
# Also appears in: Slip 11 (PDF Page 13) - Q2 [20 Marks]
#
# QUESTION:
# Q2. Apply Logistic Regression to classify smartphones into different
# price categories using
# specifications such as RAM, storage, battery capacity, and camera
# resolution. Assess the model
# using Accuracy, F1-Score, and Confusion Matrix.
#
# [20 Marks]
# ============================================================================

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from sklearn.datasets import make_classification

p = "datasets/train.csv" if os.path.exists("datasets/train.csv") else ("datasets/mobile_price.csv" if os.path.exists("datasets/mobile_price.csv") else "train.csv")
try:
    df = pd.read_csv(p)
    feats = [c for c in ["ram", "int_memory", "battery_power", "pc", "px_height", "px_width"] if c in df.columns]
    X, y = df[feats], df["price_range"]
except Exception:
    X, y = make_classification(n_samples=100, n_features=4, n_classes=4, n_informative=4, n_redundant=0, random_state=42)

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=42)
clf = LogisticRegression(max_iter=1000).fit(X_tr, y_tr)
preds = clf.predict(X_te)

print("Accuracy :", accuracy_score(y_te, preds))
print("F1-Score :", f1_score(y_te, preds, average="weighted"))
print("Confusion Matrix:\n", confusion_matrix(y_te, preds))
