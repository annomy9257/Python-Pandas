"""
Write a program to create a Series using a list object, input
numbers into it, and print the sum of all odd numbers in the
Series.
"""

import pandas as pd

shakya_lst = []
for i in range(5):
    shakya_lst.append(int(input()))

shakya_s = pd.Series(shakya_lst)
print(shakya_s[shakya_s % 2 != 0].sum())

"""
OUTPUT:
"""