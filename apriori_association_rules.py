# ============================================================================
# Slip 02 (PDF Page 4) - Q2 (OR) [20 Marks]
# Also appears in: Slip 10 (PDF Page 12) - Q2 (OR) [20 Marks]
#
# QUESTION:
# Q2. Create the following dataset in python. Apply the Apriori algorithm
# to generate frequent itemsets
# and association rules. Repeat the process with different minimum support
# values 0.2, and 0.3.
#
# [20 Marks]
#
# TID Items
# 1 Video Lecture, Quiz
# 2 Video Lecture, Assignment
# 3 Quiz, Discussion Forum
# 4 Video Lecture, Quiz, Assignment
# 5 Assignment, Discussion Forum
# 6 Video Lecture, Certificate
# 7 Quiz, Certificate
# 8 Video Lecture, Quiz
# 9 Assignment, Certificate
# 10 Video Lecture, Quiz, Certificate
# ============================================================================

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

dataset = [
    ["Video Lecture", "Quiz"],
    ["Video Lecture", "Assignment"],
    ["Quiz", "Discussion Forum"],
    ["Video Lecture", "Quiz", "Assignment"],
    ["Assignment", "Discussion Forum"],
    ["Video Lecture", "Certificate"],
    ["Quiz", "Certificate"],
    ["Video Lecture", "Quiz"],
    ["Assignment", "Certificate"],
    ["Video Lecture", "Quiz", "Certificate"]
]

te = TransactionEncoder()
df = pd.DataFrame(te.fit_transform(dataset), columns=te.columns_)

for s in [0.2, 0.3, 0.4]:
    print(f"\n--- Min Support: {s} ---")
    freq = apriori(df, min_support=s, use_colnames=True)
    print(freq)
    if not freq.empty:
        rules = association_rules(freq, metric="confidence", min_threshold=0.5)
        print(rules[["antecedents", "consequents", "support", "confidence"]])
