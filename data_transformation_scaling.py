# ============================================================================
# Slip 16 (PDF Page 18) - Q2 [20 Marks]
# Also appears in: Slip 19 (PDF Page 21) - Q2 [20 Marks], Slip 23 (PDF Page 25) - Q2 [20 Marks]
#
# QUESTION:
# Q2. Write a Python program to create a DataFrame with the attributes
# Temperature, Humidity, Wind-
# Speed, Pressure, and Rainfall. Apply the following data transformation
# techniques and display
# the transformed data:
#
# a)Min-MaxScaling
# b)Standardization
# c) Normalization
#
# [20 Marks]
# ============================================================================

import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, Normalizer

df = pd.DataFrame({
    "Temperature": [25.5, 30.2, 22.0, 35.8],
    "Humidity": [80.0, 65.0, 90.0, 45.0],
    "Wind Speed": [12.0, 18.5, 8.0, 25.0],
    "Pressure": [1012, 1008, 1015, 1005],
    "Rainfall": [15, 2, 28, 0]
})

print("Min-Max Scaled:\n", pd.DataFrame(MinMaxScaler().fit_transform(df), columns=df.columns))
print("\nStandardized:\n", pd.DataFrame(StandardScaler().fit_transform(df), columns=df.columns))
print("\nNormalized:\n", pd.DataFrame(Normalizer().fit_transform(df), columns=df.columns))
