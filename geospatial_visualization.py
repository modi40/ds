# ============================================================================
# Slip 08 (PDF Page 10) - Q1 [10 Marks]
#
# QUESTION:
# Q1. Create a suitable dataset containing information about earthquakes
# using Latitude, Longitude,
# Depth, and Magnitude. Perform the following tasks:
# a. Create a Geospatial Visualization to display the locations of
# earthquakes on a map.
# b. Use color to represent the magnitude of each earthquake.
# [10 Marks]
# ============================================================================

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Latitude": [28.39, 35.67, -6.20, 37.77, -33.86, 19.07, 39.90, -12.04],
    "Longitude": [84.12, 139.65, 106.84, -122.41, 151.20, 72.87, 116.40, -77.04],
    "Depth": [15, 40, 22, 8, 12, 18, 11, 35],
    "Magnitude": [7.8, 6.5, 5.8, 4.9, 5.2, 4.5, 6.1, 7.1]
})

plt.figure(figsize=(8, 5))
scatter = plt.scatter(df["Longitude"], df["Latitude"], c=df["Magnitude"], cmap="Reds", s=df["Magnitude"]**2 * 8, edgecolors="black")
plt.colorbar(scatter, label="Magnitude")
plt.title("Geospatial Visualization of Earthquakes")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()
