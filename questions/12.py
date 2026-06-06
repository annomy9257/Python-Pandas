"""
Write a program to create a Series using a list object, input
numbers into it, and print the sum of all odd numbers in the
Series.
"""

import pandas as pd

shakya_lst = []
for i in range(5):
    shakya_lst.append(int(input("Enter a number: ")))

shakya_s = pd.Series(shakya_lst)
print("Sum of odd numbers:", shakya_s[shakya_s % 2 != 0].sum())

"""
OUTPUT:
Enter a number: 1
Enter a number: 2
Enter a number: 3
Enter a number: 4
Enter a number: 5
Sum of odd numbers: 9
"""