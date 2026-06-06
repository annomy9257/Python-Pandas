"""
Write a program to create a DataFrame named Students using
a list containing the names and marks of 5 students.
"""

import pandas as pd

data = [["Amit", 85], ["Bhavna", 92], ["Chetan", 78], ["Divya", 95], ["Esha", 88]]
Students = pd.DataFrame(data, columns=["Name", "Marks"])
print(Students)

"""
OUTPUT:
     Name  Marks
0    Amit     85
1  Bhavna     92
2  Chetan     78
3   Divya     95
4    Esha     88
"""