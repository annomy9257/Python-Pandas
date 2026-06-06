"""
Write a program to create a Pandas Series from a dictionary
and an ndarray.
"""

import numpy as np
import pandas as pd

# From dictionary
dict_data = {"A": 10, "B": 20, "C": 30}
s_dict = pd.Series(dict_data)
print(s_dict)

# From ndarray
array_data = np.array([100, 200, 300])
s_array = pd.Series(array_data)
print(s_array)

"""
OUTPUT:
A    10
B    20
C    30
dtype: int64
0    100
1    200
2    300
dtype: int64
"""