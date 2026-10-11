# ============================================================================
# Slip 16 (PDF Page 18) - Q1 [10 Marks]
#
# QUESTION:
# Q1. Create a DataFrame containing student performance data with
# attributes such as Study Hours,
# Attendance, Assignment Score, and Exam Score. Calculate the correlation
# matrix for these
# attributes and generate a Heat Map to visualize the correlation between
# them. Display the
# correlation values, suitable labels, and an appropriate title.
# [10 Marks]
# ============================================================================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Study Hours": [2.5, 5.1, 3.2, 8.5, 3.5, 1.5, 9.2, 5.5, 8.3, 2.7],
    "Attendance": [75, 85, 70, 95, 80, 60, 98, 88, 92, 72],
    "Assignment Score": [70, 80, 65, 92, 74, 50, 95, 85, 90, 68],
    "Exam Score": [68, 82, 64, 95, 76, 52, 97, 86, 93, 70]
})

corr = df.corr()
print("Correlation Matrix:\n", corr)

plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap: Student Performance")
plt.tight_layout()
plt.show()
