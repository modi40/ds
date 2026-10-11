# ============================================================================
# Slip 24 (PDF Page 26) - Q1 [10 Marks]
#
# QUESTION:
# Q1. Write a Python program to create a book_records DataFrame containing
# the attributes Book_ID
# and Book_Price for suitable sample records. Perform Data Discretization
# on the Book_Price
# attribute using Equal Width Binning. Display the original and
# discretized data.
# [10 Marks]
# ============================================================================

import pandas as pd

book_records = pd.DataFrame({
    "Book_ID": [201, 202, 203, 204, 205, 206, 207, 208],
    "Book_Price": [150, 220, 310, 450, 580, 750, 890, 1200]
})

book_records["Price_Binned"] = pd.cut(book_records["Book_Price"], bins=3)
print("Equal Width Binning on Book Price:\n", book_records)
