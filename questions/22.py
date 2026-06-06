"""
Write a program to export data from Pandas to a CSV file.
"""

import pandas as pd

data = {"Name": ["Amit", "Bhavna"], "Marks": [85, 92]}
df = pd.DataFrame(data)

df.to_csv("student_data.csv", index=False)