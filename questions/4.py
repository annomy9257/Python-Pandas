"""
Write a program to generate a series of marks of 6 students.
Give moderation up to 5 marks of those who are having
marks < 90 and print the new list of the marks. 
"""

import pandas as pd

shakya = pd.Series([88, 92, 75, 89, 95, 60])
shakya[shakya < 90] += 5
print(shakya)

"""
OUTPUT:
0    93
1    92
2    80
3    94
4    95
5    65
dtype: int64
"""