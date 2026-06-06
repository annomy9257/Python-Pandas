"""
Write a program to create a Series and print the bottom 3
elements using the tail() function. 
"""

import pandas as pd

shakya_s = pd.Series([11, 22, 33, 44, 55, 66, 77])
print(shakya_s.tail(3))