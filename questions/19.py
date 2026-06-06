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

"""
OUTPUT:
   Roll_No    Name  Marks
0      101    Amit     85
1      102  Bhavna     92
2      103  Chetan     78
   Roll_No   Name  Marks
3      104  Divya     95
4      105   Esha     88
"""