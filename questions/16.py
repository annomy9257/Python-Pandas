"""
Write a program to create a DataFrame named Countries using
a dictionary that stores country names, capitals, and populations.
"""

import pandas as pd

sk = {
    "Country": ["India", "United States", "Japan", "Germany"],
    "Capital": ["New Delhi", "Washington, D.C.", "Tokyo", "Berlin"],
    "Population": [1440000000, 341000000, 124000000, 84000000],
}

countries = pd.DataFrame(sk)
print(countries)

"""
OUTPUT:
"""