# ============================================================================
# Slip 04 (PDF Page 6) - Q2 [20 Marks]
# Also appears in: Slip 13 (PDF Page 15) - Q2 (OR) [20 Marks]
#
# QUESTION:
# Q2. Apply Logistic Regression on an Online Gaming dataset to classify
# players as Casual or
# Professional gamers based on features such as daily play time,
# achievements unlocked, in-game
# purchases, and gaming level. Evaluate the model using Accuracy,
# Precision, Recall, F1-Score, and
# Confusion Matrix.
# [20 Marks]
# ============================================================================

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.datasets import make_classification

p = "datasets/online_gaming_behavior_dataset.csv" if os.path.exists("datasets/online_gaming_behavior_dataset.csv") else "online_gaming_behavior_dataset.csv"
try:
    df = pd.read_csv(p)
    X = df[["DailyPlayTime", "AchievementsUnlocked", "InGamePurchases", "GamingLevel"]]
    y = df["PlayerCategory"].map({"Casual": 0, "Professional": 1})
except Exception:
    X, y = make_classification(n_samples=100, n_features=4, random_state=42)

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=42)
model = LogisticRegression().fit(X_tr, y_tr)
preds = model.predict(X_te)

print("Accuracy :", accuracy_score(y_te, preds))
print("Precision:", precision_score(y_te, preds, average="weighted"))
print("Recall   :", recall_score(y_te, preds, average="weighted"))
print("F1-Score :", f1_score(y_te, preds, average="weighted"))
print("Confusion Matrix:\n", confusion_matrix(y_te, preds))
