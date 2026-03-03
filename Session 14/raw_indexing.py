# Raw indexing can be accessed using either iloc or loc
import pandas as pd

df = pd.read_csv("employee.csv")
#print(df)

# to print raws
x = df.iloc[0:3]# u can also search single raw
print(x)
# if index is manual then use loc
df.index = ['a','b','c','d','e','f','g']

y = df.loc['b':'d']#  u can also search single raw
print(y)