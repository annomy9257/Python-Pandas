"""
Write a program to create a Series using a list object, input
numbers into it, and print the sum of all odd numbers in the
Series.
"""

import pandas as pd

lst = [int(x) for x in input().split()]
s = pd.Series(lst)
print(s[s % 2 != 0].sum())