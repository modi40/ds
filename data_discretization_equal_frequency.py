# ============================================================================
# Slip 15 (PDF Page 17) - Q1 [10 Marks]
#
# QUESTION:
# Q1. Write a Python program to create an age_records DataFrame containing
# the attributes Person_ID
# and Age for suitable sample records. Perform Data Discretization on the
# Age attribute using
# Equal Frequency Binning. Display the original and discretized data.
# [10 Marks]
# ============================================================================

import pandas as pd

age_records = pd.DataFrame({
    "Person_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Age": [19, 23, 27, 31, 36, 42, 53, 68]
})

age_records["Discretized_Age"] = pd.qcut(age_records["Age"], q=3)
print("Equal Frequency Binning:\n", age_records)
