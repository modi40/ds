# ============================================================================
# Slip 07 (PDF Page 9) - Q1 [10 Marks]
# Also appears in: Slip 25 (PDF Page 27) - Q1 [10 Marks]
#
# QUESTION:
# Q1. Consider the following dataset representing the number of students
# enrolled in different courses:
# courses = ["BCA", "BBA", "B.Com", "B.Sc", "BA"]
# students = [60, 45, 75, 50, 35]
# Create a Bar Chart to visualize the number of students enrolled in each
# course. Use different bar
# colors, add an appropriate title, and label both axes.
# [10 Marks]
# ============================================================================

import matplotlib.pyplot as plt

courses = ["BCA", "BBA", "B.Com", "B.Sc", "BA"]
students = [60, 45, 75, 50, 35]

plt.figure(figsize=(7, 4))
plt.bar(courses, students, color=["blue", "green", "red", "purple", "orange"])
plt.title("Student Enrollment in Courses")
plt.xlabel("Courses")
plt.ylabel("Number of Students")
plt.show()
