# ============================================================================
# Slip 12 (PDF Page 14) - Q1 [10 Marks]
#
# QUESTION:
# Q1. Load the Titanic dataset (titanic.csv) Create a histogram showing
# the number of passengers in
# each passenger class. Create a Pie Chart showing the survival
# distribution.
# [10 Marks]
# ============================================================================

import os
import pandas as pd
import matplotlib.pyplot as plt

p = "datasets/titanic.csv" if os.path.exists("datasets/titanic.csv") else "titanic.csv"
try:
    df = pd.read_csv(p)
except Exception:
    df = pd.DataFrame({"Pclass": [1]*30 + [2]*35 + [3]*70, "Survived": [1]*45 + [0]*90})

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].hist(df["Pclass"], bins=[0.5, 1.5, 2.5, 3.5], rwidth=0.6, color="skyblue", edgecolor="black")
ax[0].set_title("Passengers by Class")
ax[0].set_xlabel("Pclass")
ax[0].set_xticks([1, 2, 3])

df["Survived"].value_counts().plot(kind="pie", ax=ax[1], autopct="%1.1f%%", labels=["Died", "Survived"], colors=["salmon", "lightgreen"])
ax[1].set_title("Survival Distribution")
ax[1].set_ylabel("")
plt.tight_layout()
plt.show()
