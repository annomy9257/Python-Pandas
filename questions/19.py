"""
Write a program to create a DataFrame for examination results
and display the first 3 rows and last 2 rows of the DataFrame
using the head() and tail() functions.
"""

import pandas as pd

data = {
    "Roll_No": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Bhavna", "Chetan", "Divya", "Esha"],
    "Marks": [85, 92, 78, 95, 88],
}
df = pd.DataFrame(data)

print(df.head(3))
print(df.tail(2))