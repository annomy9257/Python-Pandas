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