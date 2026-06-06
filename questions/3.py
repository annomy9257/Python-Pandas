"""
Write a program to create a Series and find the sum of all
values ending with 5.
"""

import pandas as pd

s = pd.Series([15, 22, 35, 40, 55])
print(s[s % 10 == 5].sum())

"""
OUTPUT:
105
"""