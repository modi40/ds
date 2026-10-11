# ============================================================================
# Slip 11 (PDF Page 13) - Q1 [10 Marks]
#
# QUESTION:
# Q1. An organization has recorded the number of employees working in
# different departments such as
# HR, Finance, IT, Sales, and Marketing. Write a Python program to create
# a bar chart showing the
# distribution of employees among these departments. Display suitable
# labels and a title.
# [10 Marks]
# ============================================================================

import matplotlib.pyplot as plt

departments = ["HR", "Finance", "IT", "Sales", "Marketing"]
employees = [25, 40, 85, 55, 30]

plt.figure(figsize=(7, 4))
plt.bar(departments, employees, color="teal")
plt.title("Distribution of Employees Among Departments")
plt.xlabel("Departments")
plt.ylabel("Number of Employees")
plt.show()
