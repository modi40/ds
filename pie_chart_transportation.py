# ============================================================================
# Slip 10 (PDF Page 12) - Q1 [10 Marks]
#
# QUESTION:
# Q1. A company conducted a survey to determine the preferred mode of
# transportation among
# employees as shown below:
# transport = [“Train", "Bicycle", "Bike", "Car", "Bus"],
# employees = [220, 60, 70, 80, 40]
# Create a Pie Chart to represent the percentage of employees using each
# mode of transportation.
# Display the percentage contribution of each category. Give appropriate
# labels and colors.
# [10 Marks]
# ============================================================================

import matplotlib.pyplot as plt

transport = ["Train", "Bicycle", "Bike", "Car", "Bus"]
employees = [220, 60, 70, 80, 40]

plt.figure(figsize=(6, 6))
plt.pie(employees, labels=transport, autopct="%1.1f%%", colors=["#386cb0", "#fdb462", "#7fc97f", "#ef3b2c", "#662506"])
plt.title("Preferred Mode of Transportation")
plt.show()
