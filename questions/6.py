"""
Write a program to create a Series of 10 numbers and
increase all elements that are multiples of 4 by 5.
"""

import pandas as pd

shakya_s = pd.Series([2, 4, 7, 8, 10, 12, 15, 16, 20, 22])
shakya_s[shakya_s % 4 == 0] += 5
print(shakya_s)