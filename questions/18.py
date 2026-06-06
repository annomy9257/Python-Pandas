"""
Write a program to create a DataFrame for examination results
and display the row labels, column labels, data types of each
column, and dimensions of the DataFrame.
"""

import pandas as pd

data = {"Roll_No": [101, 102], "Name": ["Amit", "Bhavna"], "Marks": [85, 92]}
df = pd.DataFrame(data)

print(df.index)
print(df.columns)
print(df.dtypes)
print(df.shape)

"""
OUTPUT:
RangeIndex(start=0, stop=2, step=1)
Index(['Roll_No', 'Name', 'Marks'], dtype='object')
Roll_No     int64
Name       object
Marks       int64
dtype: object
(2, 3)
"""