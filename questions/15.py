"""
Write a program to create a DataFrame named Marks from a
dictionary of marks. Locate the 2 largest values and the 3
smallest values in the DataFrame.
"""

import pandas as pd

shakya_data = {"Score": [85, 92, 78, 95, 88, 61, 70]}
shakya_marks = pd.DataFrame(shakya_data)

print(shakya_marks.sort_values(by="Score", ascending=False).head(2))
print(shakya_marks.sort_values(by="Score").head(3))

"""
OUTPUT:
   Score
3     95
1     92
   Score
5     61
6     70
2     78
"""