"""
Write a program to create a Series named Capital and
display the first 3 elements using slicing.
"""

import pandas as pd

shakya_capital = pd.Series(["New Delhi", "Washington", "London", "Paris", "Tokyo"])
print(shakya_capital[:3])

"""
OUTPUT:
0     New Delhi
1    Washington
2        London
dtype: str
"""