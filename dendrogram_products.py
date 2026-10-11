# ============================================================================
# Slip 01 (PDF Page 3) - Q1 [10 Marks]
# Also appears in: Slip 14 (PDF Page 16) - Q1 [10 Marks], Slip 23 (PDF Page 25) - Q1 [10 Marks]
#
# QUESTION:
# Q1. Create a dataframe containing information about different products
# such as Price, Rating, and
# Number of Sales. Generate a Dendrogram to group similar products based
# on their characteristics.
# [10 Marks]
# ============================================================================

import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

df = pd.DataFrame({
    "Product_name": ["Laptop", "Phone", "Headphones", "Tablet", "Watch", "Monitor"],
    "Price": [60000, 35000, 3000, 25000, 12000, 15000],
    "Rating": [4.5, 4.3, 4.0, 4.2, 3.9, 4.4],
    "Number_of_Sales": [1200, 4500, 8000, 2200, 3500, 1800]
})

linked = linkage(df[["Price", "Rating", "Number_of_Sales"]], method="ward")
plt.figure(figsize=(8, 4))
dendrogram(linked, labels=df["Product_name"].tolist())
plt.title("Dendrogram of Products")
plt.xlabel("Products")
plt.ylabel("Distance")
plt.tight_layout()
plt.show()
