# ============================================================================
# Slip 22 (PDF Page 24) - Q1 [10 Marks]
#
# QUESTION:
# Q1. Write a Python program to create a DataFrame containing the
# attributes City, House_Type,
# House_Area, Number_of_Rooms, and Monthly_Rent. Apply the Normalization
# technique to the
# numerical attributes and display the normalized data.
# [10 Marks]
# ============================================================================

import pandas as pd
from sklearn.preprocessing import Normalizer

df = pd.DataFrame({
    "City": ["Mumbai", "Pune", "Nashik", "Nagpur"],
    "House_Type": ["2BHK", "1BHK", "3BHK", "2BHK"],
    "House_Area": [850, 550, 1200, 900],
    "Number_of_Rooms": [3, 2, 4, 3],
    "Monthly_Rent": [35000, 18000, 25000, 20000]
})

num_cols = ["House_Area", "Number_of_Rooms", "Monthly_Rent"]
df[num_cols] = Normalizer().fit_transform(df[num_cols])
print("Normalized Numerical Attributes:\n", df)
