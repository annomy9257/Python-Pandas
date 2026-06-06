"""
Write a program to create a Series containing the following
numbers: 64, 55, 65, 79, 91, and 22.
"""

import pandas as pd

s = pd.Series([64, 55, 65, 79, 91, 22])
print(s)

"""
OUTPUT:
0    64
1    55
2    65
3    79
4    91
5    22
dtype: int64
"""