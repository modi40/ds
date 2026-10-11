# ============================================================================
# Slip 07 (PDF Page 9) - Q2 (OR) [20 Marks]
# Also appears in: Slip 15 (PDF Page 17) - Q2 (OR) [20 Marks], Slip 25 (PDF Page 27) - Q2 (OR) [20 Marks]
#
# QUESTION:
# Q2. Write a Python program to perform market basket analysis on the
# Groceries dataset using the
# Apriori algorithm. Read and explore the dataset, preprocess the data by
# handling missing values,
# convert categorical transaction data into a suitable numeric format, and
# generate frequent itemsets
# and association rules. Repeat the analysis using minimum support values
# 0.3 and 0.4.
#
# [20 Marks]
#
# S.No. Items Purchased
# 1 Basmati Rice, Toor Dal, Turmeric Powder, Cooking Oil
# 2 Atta, Sugar, Tea, Milk
# 3 Rice, Moong Dal, Salt, Cooking Oil
# 4 Wheat Flour, Chickpeas, Turmeric Powder, Cumin Seeds
# 5 Poha, Peanuts, Onions, Cooking Oil
# 6 Basmati Rice, Paneer, Garam Masala, Tomatoes
# 7 Atta, Potatoes, Onions, Cooking Oil
# ============================================================================

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

transactions = [
    ["Basmati Rice", "Toor Dal", "Turmeric Powder", "Cooking Oil"],
    ["Atta", "Sugar", "Tea", "Milk"],
    ["Rice", "Moong Dal", "Salt", "Cooking Oil"],
    ["Wheat Flour", "Chickpeas", "Turmeric Powder", "Cumin Seeds"],
    ["Poha", "Peanuts", "Onions", "Cooking Oil"],
    ["Basmati Rice", "Paneer", "Garam Masala", "Tomatoes"],
    ["Atta", "Potatoes", "Onions", "Cooking Oil"]
]

te = TransactionEncoder()
df = pd.DataFrame(te.fit_transform(transactions), columns=te.columns_)

for s in [0.3, 0.4]:
    print(f"\n--- Min Support: {s} ---")
    freq = apriori(df, min_support=s, use_colnames=True)
    print(freq)
    if not freq.empty:
        rules = association_rules(freq, metric="confidence", min_threshold=0.5)
        print(rules[["antecedents", "consequents", "support", "confidence"]])
