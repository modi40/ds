# ============================================================================
# Slip 17 (PDF Page 19) - Q1 [10 Marks]
#
# QUESTION:
# Q1. Write a Python program to create two DataFrames, student_details and
# academic_records ,
# containing suitable student -related attributes. Perform data
# integration by combining the two
# DataFrames using a common attribute such as Student_ID. Display the
# individual DataFrames
# and the integrated DataFrame.
# [10 Marks]
# ============================================================================

import pandas as pd

student_details = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104],
    "Name": ["Aarav", "Ananya", "Rohan", "Sneha"],
    "Department": ["CS", "DS", "IT", "CS"]
})

academic_records = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104],
    "CGPA": [8.9, 9.2, 7.8, 8.5],
    "Attendance": [92, 95, 80, 88]
})

integrated = pd.merge(student_details, academic_records, on="Student_ID")
print("Integrated DataFrame:\n", integrated)
