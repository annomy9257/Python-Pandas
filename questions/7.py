"""
Write a program to create a Series and print the top 3
elements using the head() function.
"""

import pandas as pd

s = pd.Series([10, 20, 30, 40, 50, 60, 70])
print(s.head(3))