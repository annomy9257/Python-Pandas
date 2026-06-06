"""
Write a program to create a Series of 10 numbers and
increase all elements that are multiples of 4 by 5.
"""

import pandas as pd

# 1. Create a Series of 10 numbers
shakya_list = [2, 4, 7, 8, 10, 12, 15, 16, 20, 22]
shakya_series = pd.Series(shakya_list)

print("--- Original Shakya Series ---")
print(shakya_series)

# 2. Increase all elements that are multiples of 4 by 5
# Condition: shakya_series % 4 == 0
shakya_series[shakya_series % 4 == 0] += 5

print("\n--- Modified Shakya Series ---")
print(shakya_series)