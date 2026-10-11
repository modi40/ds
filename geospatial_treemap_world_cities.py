# ============================================================================
# Slip 18 (PDF Page 20) - Q2 [20 Marks]
# Also appears in: Slip 24 (PDF Page 26) - Q2 [20 Marks]
#
# QUESTION:
# Q2. Consider the World Cities dataset containing attributes - city,
# country, latitude, longitude, and
# population information. Perform the following tasks:
# a. Create a Geospatial Visualization showing the locations of cities on
# a world map, using
# marker size to represent population.
# b. Create a Treemap to visualize the population distribution of cities.
#
# [20 Marks]
# ============================================================================

import os
import pandas as pd
import matplotlib.pyplot as plt
import squarify

p = "datasets/worldcities.csv" if os.path.exists("datasets/worldcities.csv") else "worldcities.csv"
try:
    df = pd.read_csv(p)
except Exception:
    df = pd.DataFrame({
        "city": ["Tokyo", "Delhi", "Shanghai", "Sao Paulo", "Mumbai", "Cairo"],
        "latitude": [35.68, 28.61, 31.23, -23.55, 19.07, 30.04],
        "longitude": [139.69, 77.20, 121.47, -46.63, 72.87, 31.23],
        "population": [37400000, 30290000, 27050000, 22040000, 20410000, 20900000]
    })

top = df.sort_values(by="population", ascending=False).head(8)

plt.figure(figsize=(7, 4))
plt.scatter(top["longitude"], top["latitude"], s=top["population"]/200000, color="orange", edgecolors="black")
for _, r in top.iterrows():
    plt.annotate(r["city"], (r["longitude"], r["latitude"]))
plt.title("World Cities Locations and Population")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()

plt.figure(figsize=(7, 4))
squarify.plot(sizes=top["population"], label=top["city"], alpha=0.8)
plt.axis("off")
plt.title("Population Distribution Treemap")
plt.show()
