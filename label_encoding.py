# ============================================================================
# Slip 05 (PDF Page 7) - Q1 [10 Marks]
#
# QUESTION:
# Q1. Write a Python program to create a customer_DataFrame with suitable
# attributes such as
# Customer_ID, Gender, City, and Membership_Type. Perform label encoding
# technique on
# appropriate categorical attributes. Display the DataFrame before and
# after encoding.
#
# [10 Marks]
# ============================================================================

import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.DataFrame({
    "Customer_ID": [101, 102, 103, 104],
    "Gender": ["Male", "Female", "Female", "Male"],
    "City": ["Pune", "Mumbai", "Nashik", "Pune"],
    "Membership_Type": ["Gold", "Silver", "Platinum", "Silver"]
})

print("Before Encoding:\n", df)
le = LabelEncoder()
for col in ["Gender", "City", "Membership_Type"]:
    df[col] = le.fit_transform(df[col])
print("\nAfter Label Encoding:\n", df)
