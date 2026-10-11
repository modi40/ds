# ============================================================================
# Slip 05 (PDF Page 7) - Q2 [20 Marks]
# Also appears in: Slip 22 (PDF Page 24) - Q2 [20 Marks]
#
# QUESTION:
# Q2. Generate a DataFra me containing customer information for Netflix
# and Amazon Prime users.
# Create a Venn diagram and a Pie chart to show the customers using only
# Netflix, only Amazon
# Prime, and both services. Add appropriate labels, colors, and titles to
# both visualizations.
#
# [20 Marks]
# ============================================================================

import matplotlib.pyplot as plt
from matplotlib_venn import venn2

netflix = {"Alice", "Bob", "Charlie", "David", "Emma", "Frank"}
prime = {"David", "Emma", "Frank", "George", "Hannah", "Ian"}

only_n = len(netflix - prime)
only_p = len(prime - netflix)
both = len(netflix & prime)

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
venn2(subsets=(only_n, only_p, both), set_labels=("Netflix", "Amazon Prime"), ax=ax[0])
ax[0].set_title("Venn Diagram")

ax[1].pie([only_n, only_p, both], labels=["Only Netflix", "Only Prime", "Both"], autopct="%1.1f%%")
ax[1].set_title("Subscription Share")
plt.tight_layout()
plt.show()
