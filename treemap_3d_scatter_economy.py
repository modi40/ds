# ============================================================================
# Slip 17 (PDF Page 19) - Q2 [20 Marks]
#
# QUESTION:
# Q2. Create a dataset containing information about different cities with
# the attributes: City, Population,
# GDP, and Literacy Rate. Perform the following visualization tasks:
# a. Generate a Treemap showing city-wise population distribution.
# b. Create a 3D Scatter Plot using Population, GDP, and Literacy Rate.
# [20 Marks]
# ============================================================================

import pandas as pd
import matplotlib.pyplot as plt
import squarify

df = pd.DataFrame({
    "City": ["Mumbai", "Delhi", "Bengaluru", "Hyderabad", "Chennai", "Kolkata"],
    "Population": [12.5, 11.0, 8.4, 6.8, 7.1, 4.5],
    "GDP": [310, 293, 110, 75, 78, 60],
    "Literacy Rate": [89.7, 86.2, 88.7, 83.2, 90.2, 87.1]
})

plt.figure(figsize=(7, 4))
squarify.plot(sizes=df["Population"], label=df["City"], alpha=0.8)
plt.axis("off")
plt.title("City-wise Population Treemap")
plt.show()

fig = plt.figure(figsize=(7, 5))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(df["Population"], df["GDP"], df["Literacy Rate"], c="teal", s=80)
for _, r in df.iterrows():
    ax.text(r["Population"], r["GDP"], r["Literacy Rate"], r["City"])
ax.set_xlabel("Population (M)")
ax.set_ylabel("GDP (B$)")
ax.set_zlabel("Literacy Rate (%)")
ax.set_title("3D Scatter: Population, GDP, Literacy")
plt.show()
