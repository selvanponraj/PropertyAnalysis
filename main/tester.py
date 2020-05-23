import pandas as pd

import numpy as np

## testing
df1 = {
    'State': ['Arizona AZ', 'Georgia GG', 'Newyork NY', 'Indiana IN', 'Florida FL'],
    'Score': [62, 47, 55, 74, 31]}

df1 = pd.DataFrame(df1, columns=['State', 'Score'])
print(df1)
df1['state_substring'] =df1.State.str.slice(0, 7)

print(df1)
