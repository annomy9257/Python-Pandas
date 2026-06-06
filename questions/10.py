"""
Write a Python program to create a Series storing the
percentages of 4 students using a dictionary, and print all
elements with percentages above 85.
"""

import pandas as pd

shakya_data = {"Student A": 82, "Student B": 91, "Student C": 78, "Student D": 88}
s = pd.Series(shakya_data)
print(s[s > 85])

"""
OUTPUT:
Student B    91
Student D    88
dtype: int64
"""