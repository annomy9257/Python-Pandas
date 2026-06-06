"""
Write a Pandas program to perform arithmetic operations on
two Pandas Series.
"""

import pandas as pd

shakya_s1 = pd.Series([10, 20, 30, 40])
shakya_s2 = pd.Series([2, 4, 5, 8])

print(shakya_s1 + shakya_s2)
print(shakya_s1 - shakya_s2)
print(shakya_s1 * shakya_s2)
print(shakya_s1 / shakya_s2)

"""
OUTPUT:

0    12
1    25
2    36
dtype: int64
0     8
1    15
2    24
dtype: int64
0     20
1    100
2    180
dtype: int64
0    5.0
1    4.0
2    5.0
dtype: float64
"""