# ============================================================================
# Slip 06 (PDF Page 8) - Q1 [10 Marks]
#
# QUESTION:
# Q1. Create a DataFrame containing the car model, engine size (in
# litres), and fuel efficiency (in km/L)
# for the given cars. Create a scatter plot to visualize the relationship
# between engine size and
# fuel efficiency.Add an appropriate title, label both axes, and use
# different colors for the
# data points.
# [10 Marks]
# ============================================================================

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Model": ["Swift", "i20", "City", "Nexon", "Fortuner", "XUV700", "EcoSport"],
    "Engine_Size": [1.2, 1.0, 1.5, 1.2, 2.8, 2.0, 1.5],
    "Fuel_Efficiency": [22.0, 20.0, 18.0, 17.5, 12.0, 13.5, 16.0]
})

colors = ["red", "blue", "green", "purple", "orange", "brown", "cyan"]
plt.figure(figsize=(7, 4))
plt.scatter(df["Engine_Size"], df["Fuel_Efficiency"], c=colors, s=80)
plt.title("Engine Size vs Fuel Efficiency")
plt.xlabel("Engine Size (Litres)")
plt.ylabel("Fuel Efficiency (km/L)")
plt.show()
