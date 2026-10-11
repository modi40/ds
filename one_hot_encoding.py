# ============================================================================
# Slip 14 (PDF Page 16) - Q2 (OR) [20 Marks]
# Also appears in: Slip 25 (PDF Page 27) - Q2 [20 Marks]
#
# QUESTION:
# Q2. Create two DataFrames containing information about different mobile
# phones.
# DataFrame 1: Brand, Model, Price, RAM
# DataFrame 2: Model, Storage, Battery_Capacity, Operating_System
#
# Perform the following data transformation techniques:
# a) Data Integration by combining the two DataFrames using Model
# b) Label Encoding on the Brand attribute of the merged DataFrame
# c) One-Hot Encoding on the Operating_System attribute of the merged
# DataFrame
# Display the original DataFrames, merged DataFrame, and transformed
# DataFrame.
# [20 Marks]
# ============================================================================

import pandas as pd
from sklearn.preprocessing import LabelEncoder

df1 = pd.DataFrame({
    "Brand": ["Apple", "Samsung", "OnePlus", "Xiaomi"],
    "Model": ["iPhone 13", "Galaxy S21", "Nord 2", "Redmi Note 11"],
    "Price": [69900, 54999, 29999, 14999],
    "RAM": ["4GB", "8GB", "8GB", "6GB"]
})

df2 = pd.DataFrame({
    "Model": ["iPhone 13", "Galaxy S21", "Nord 2", "Redmi Note 11"],
    "Storage": ["128GB", "128GB", "128GB", "64GB"],
    "Battery_Capacity": ["3240mAh", "4000mAh", "4500mAh", "5000mAh"],
    "Operating_System": ["iOS", "Android", "Android", "Android"]
})

merged = pd.merge(df1, df2, on="Model")
merged["Brand"] = LabelEncoder().fit_transform(merged["Brand"])
transformed = pd.get_dummies(merged, columns=["Operating_System"])

print("Merged Data (Integration):\n", merged)
print("\nTransformed Data (Label & One-Hot Encoded):\n", transformed)
