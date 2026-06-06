"""
Write a program to import data from a CSV file into Pandas
"""

import pandas as pd

file_path = "assets/data.csv"
# I created the file_path variable and used "assets/data.csv" because I have stored the file in a folder named "assets". If you don't want to use a folder, make sure your "data.csv" file is in the same folder or path as your Python script, and then you can simply use "data.csv" as the file path.

df = pd.read_csv(file_path)
print(df)