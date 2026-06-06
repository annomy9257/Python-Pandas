"""
Write a program to export data from Pandas to a CSV file.
"""

import pandas as pd

data = {"Name": ["Amit", "Bhavna"], "Marks": [85, 92]}
df = pd.DataFrame(data)

df.to_csv("student_data.csv", index=False)

"""
OUTPUT:
This code saves the DataFrame to a CSV file named "student_data.csv" in the current working directory. The index=False parameter is used to prevent the index from being written to the CSV file.
"""