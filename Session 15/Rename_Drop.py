import pandas as pd

df = pd.read_csv("Sales_data.csv")
#print(df)
Rename = df.rename(columns={'Price':'UnitPrice', 'Customer': "Name"})
print(Rename)

Drop = df.drop(columns=['Orderdate'])
print(Drop)