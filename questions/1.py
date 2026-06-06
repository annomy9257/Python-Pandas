"""
Write a program to generate a series of the first 10 integers.
"""

import pandas as pd

s = pd.Series(range(1, 11))
print(s)

"""
OUTPUT:
0     1
1     2
2     3
3     4
4     5
5     6
6     7
7     8
8     9
9    10
dtype: int64
"""