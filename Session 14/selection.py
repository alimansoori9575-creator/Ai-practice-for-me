import pandas as pd

df = pd.read_csv("employee.csv")
print(df)
# to print column
x = df['role']
print(x)

y = df[['name','age']]
print(y)