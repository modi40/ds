# ============================================================================
# Slip 02 (PDF Page 4) - Q1 [10 Marks]
#
# QUESTION:
# Q1. Write a Python program to create an age_records DataFrame containing
# the attributes Person_ID
# and Age for suitable sample records. Perform Data Discretization on the
# Age attribute using
# Equal Width Binning. Display the original and discretized data.
# [10 Marks]
# ============================================================================

import pandas as pd

age_records = pd.DataFrame({
    "Person_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Age": [18, 22, 25, 30, 35, 42, 55, 68]
})

age_records["Discretized_Age"] = pd.cut(age_records["Age"], bins=3)
print("Equal Width Binning:\n", age_records)
