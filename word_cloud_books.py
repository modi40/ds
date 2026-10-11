# ============================================================================
# Slip 09 (PDF Page 11) - Q2 (OR) [20 Marks]
# Also appears in: Slip 20 (PDF Page 22) - Q2 [20 Marks]
#
# QUESTION:
# Q2. Create a dataset containing information about different books with
# the attributes Book Title,
# Author, Publication Year, Average Rating, and Number of Ratings.
# Perform the following tasks on created dataset:
# a. Create a Venn Diagram comparing the authors of books published in two
# different time
# periods.
# b. Generate a Word Cloud using the book titles.
# [20 Marks]
# ============================================================================

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from matplotlib_venn import venn2

df = pd.DataFrame({
    "Book Title": ["Data Science Handbook", "Python Machine Learning", "Deep Learning Secrets", "AI Basics", "Big Data", "Algorithms"],
    "Author": ["Jake", "Sebastian", "Ian", "Stuart", "Jake", "Thomas"],
    "Publication Year": [1998, 2015, 2016, 1995, 2005, 2001]
})

p1 = set(df[df["Publication Year"] < 2010]["Author"])
p2 = set(df[df["Publication Year"] >= 2010]["Author"])

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
venn2([p1, p2], set_labels=("Pre-2010", "2010+"), ax=ax[0])
ax[0].set_title("Authors Comparison")

wc = WordCloud(background_color="white").generate(" ".join(df["Book Title"]))
ax[1].imshow(wc, interpolation="bilinear")
ax[1].axis("off")
ax[1].set_title("Word Cloud of Book Titles")
plt.tight_layout()
plt.show()
