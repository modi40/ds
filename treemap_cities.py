# ============================================================================
# Slip 15 (PDF Page 17) - Q2 [20 Marks]
#
# QUESTION:
# Q2. Create a DataFrame containing information about different cities
# with the attributes City, Area
# (sq. km), Average Temperature (°C), Rainfall (mm), and Population
# Density. Generate a
# Treemap to visualize the population density of each city and create a 3D
# Scatter Plot using Area,
# Average Temperature, and Rainfall. Add suitable labels, colors, and
# titles to both visualizations.
#
# [20 Marks]
# ============================================================================

import pandas as pd
import matplotlib.pyplot as plt
import squarify

df = pd.DataFrame({
    "City": ["Mumbai", "Delhi", "Bengaluru", "Kolkata", "Chennai", "Pune"],
    "Area": [603, 1484, 741, 206, 426, 331],
    "Average Temperature": [27.2, 25.0, 23.6, 26.8, 28.6, 24.5],
    "Rainfall": [2200, 790, 970, 1750, 1400, 722],
    "Population Density": [21000, 11320, 4381, 24000, 14350, 9400]
})

plt.figure(figsize=(7, 4))
squarify.plot(sizes=df["Population Density"], label=df["City"], alpha=0.8)
plt.axis("off")
plt.title("City Population Density Treemap")
plt.show()

fig = plt.figure(figsize=(7, 5))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(df["Area"], df["Average Temperature"], df["Rainfall"], c=df["Population Density"], cmap="viridis", s=80)
for _, r in df.iterrows():
    ax.text(r["Area"], r["Average Temperature"], r["Rainfall"], r["City"])
ax.set_xlabel("Area")
ax.set_ylabel("Avg Temp")
ax.set_zlabel("Rainfall")
ax.set_title("3D Scatter Plot of Cities")
plt.show()
