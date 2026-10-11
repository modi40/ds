# ============================================================================
# Slip 04 (PDF Page 6) - Q1 [10 Marks]
#
# QUESTION:
# Q1. A survey was conducted to determine the preferred payment method
# among customers as shown
# below:
# payment_methods = ["UPI", "Credit Card", "Debit Card", "Cash", "Net
# Banking"]
# customers = [150, 80, 60, 40, 30]
# Create a Pie Chart to represent the percentage of customers using each
# payment method. Display
# the percentage contribution of each category and add an appropriate
# title.
# [10 Marks]
# ============================================================================

import matplotlib.pyplot as plt

payment_methods = ["UPI", "Credit Card", "Debit Card", "Cash", "Net Banking"]
customers = [150, 80, 60, 40, 30]

plt.figure(figsize=(6, 6))
plt.pie(customers, labels=payment_methods, autopct="%1.1f%%", startangle=90)
plt.title("Preferred Payment Methods")
plt.show()
