# ============================================================================
# Slip 16 (PDF Page 18) - Q2 (OR) [20 Marks]
# Also appears in: Slip 20 (PDF Page 22) - Q2 (OR) [20 Marks]
#
# QUESTION:
# Q2. Implement the Apriori algorithm on the given student activity
# dataset to identify frequent itemsets
# and generate association rules among the activities. Repeat the analysis
# using minimum support
# values 0.2 and 0.3.
# [20 Marks]
#
# TID Items
# 1. Library, Seminar
# 2. Workshop, Project
# 3. Library, Assignment
# 4. Seminar, Workshop
# 5. Assignment, Seminar
# 6. Workshop, Assignment
# 7. Project, Library
# 8. Library, Seminar, Project
# 9. Library,Seminar,Workshop
# ============================================================================

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

dataset = [
    ["Library", "Seminar"],
    ["Workshop", "Project"],
    ["Library", "Assignment"],
    ["Seminar", "Workshop"],
    ["Assignment", "Seminar"],
    ["Workshop", "Assignment"],
    ["Project", "Library"],
    ["Library", "Seminar", "Project"],
    ["Library", "Seminar", "Workshop"]
]

te = TransactionEncoder()
df = pd.DataFrame(te.fit_transform(dataset), columns=te.columns_)

for s in [0.2, 0.3]:
    print(f"\n--- Min Support: {s} ---")
    freq = apriori(df, min_support=s, use_colnames=True)
    print(freq)
    if not freq.empty:
        rules = association_rules(freq, metric="confidence", min_threshold=0.4)
        print(rules[["antecedents", "consequents", "support", "confidence"]])
