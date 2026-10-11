# ============================================================================
# Slip 09 (PDF Page 11) - Q1 [10 Marks]
#
# QUESTION:
# Q1. Write a Python program to create a product DataFrame with the
# attributes Product_ID, Price,
# Quantity_Sold, Discount, and Revenue. Apply Min-Max Scaling data
# transformation techniques
# on the DataFrame and display the transformed data.
# [10 Marks]
# ============================================================================

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.DataFrame({
    "Product_ID": [1, 2, 3, 4],
    "Price": [100, 250, 50, 800],
    "Quantity_Sold": [50, 20, 100, 5],
    "Discount": [10, 15, 5, 25],
    "Revenue": [4500, 4250, 4750, 3000]
})

cols = ["Price", "Quantity_Sold", "Discount", "Revenue"]
df[cols] = MinMaxScaler().fit_transform(df[cols])
print("Min-Max Scaled Data:\n", df)
