"""
Write a program to replace all missing values in a DataFrame
with 222.
"""

import numpy as np
import pandas as pd

data = {"A": [1, np.nan, 3], "B": [np.nan, 5, 6], "C": [7, 8, np.nan]}
shakya = pd.DataFrame(data)

shakya = shakya.fillna(222)
print(shakya)