import pandas as pd
arr = pd.Series([12, 23, 34, 45])
print(arr)
# you can add manual index
arr2 = pd.Series([12, 56, 76, 32], index=['alice', 'zaid', 'Ali', 'all'])
print(arr2)