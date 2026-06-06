"""
Write a Pandas program to perform arithmetic operations on
two Pandas Series.
"""

import pandas as pd

shakya_s1 = pd.Series([10, 20, 30, 40])
shakya_s2 = pd.Series([2, 4, 5, 8])

print("Addition:")
print(shakya_s1 + shakya_s2)

print("\nSubtraction:")
print(shakya_s1 - shakya_s2)

print("\nMultiplication:")
print(shakya_s1 * shakya_s2)

print("\nDivision:")
print(shakya_s1 / shakya_s2)