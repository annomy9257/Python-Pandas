"""
Write a program to create a Pandas DataFrame from a
dictionary and an ndarray.
"""

import numpy as np
import pandas as pd

dict_data = {"A": [1, 2, 3], "B": [4, 5, 6]}
df_dict = pd.DataFrame(dict_data)
print("DataFrame from Dictionary:")
print(df_dict)

array_data = np.array([[10, 20], [30, 40], [50, 60]])
df_array = pd.DataFrame(array_data, columns=["X", "Y"])
print("\nDataFrame from ndarray:")
print(df_array)

"""
OUTPUT:
DataFrame from Dictionary:
   A  B
0  1  4
1  2  5
2  3  6

DataFrame from ndarray:
    X   Y
0  10  20
1  30  40
2  50  60
"""