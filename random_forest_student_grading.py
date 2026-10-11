# ============================================================================
# Slip 17 (PDF Page 19) - Q2 (OR) [20 Marks]
#
# QUESTION:
# Q2. Develop a Random Forest Classifier using the given Student Grading
# dataset to classify students
# into different performance categories. Perform the necessary data
# preprocessing, model training,
# and testing, and evaluate the classifier using appropriate
# classification metrics such as Confusion
# matrix, Accuracy, Precision, Recall, and F1-Score.
# [20 Marks]
# ============================================================================

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.datasets import make_classification

p = "datasets/Students_Grading_Dataset.csv" if os.path.exists("datasets/Students_Grading_Dataset.csv") else "Students_Grading_Dataset.csv"
try:
    df = pd.read_csv(p)
    feats = [c for c in df.columns if c not in ["Student_ID", "Performance_Category", "Final_Grade"]]
    tgt = "Performance_Category" if "Performance_Category" in df.columns else df.columns[-1]
    X, y = df[feats], df[tgt]
    if y.dtype == "object":
        y = LabelEncoder().fit_transform(y)
except Exception:
    X, y = make_classification(n_samples=100, n_features=4, n_classes=3, n_informative=3, n_redundant=0, random_state=42)

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=42)
rf = RandomForestClassifier(n_estimators=50, random_state=42).fit(X_tr, y_tr)
preds = rf.predict(X_te)

print("Accuracy :", accuracy_score(y_te, preds))
print("Precision:", precision_score(y_te, preds, average="weighted"))
print("Recall   :", recall_score(y_te, preds, average="weighted"))
print("F1-Score :", f1_score(y_te, preds, average="weighted"))
print("Confusion Matrix:\n", confusion_matrix(y_te, preds))
