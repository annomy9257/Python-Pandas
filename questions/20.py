"""
Write a program to find the sum of each column and identify the
column with the lowest mean.
"""

import pandas as pd

data = {"Maths": [90, 85, 88], "Science": [78, 82, 80], "English": [95, 92, 89]}
df = pd.DataFrame(data)

# 1. Sum of each column
print(df.sum())

# 2. Column with the lowest mean
print(df.mean().idxmin())

"""
OUTPUT:
Maths      263
Science    240
English    276
dtype: int64
Science
"""