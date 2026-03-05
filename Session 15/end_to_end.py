import pandas as pd

df = pd.read_csv("Sales_data.csv")
#print(df)

#fill
df['Discount'] = df['Discount'].fillna(0)
df['Quantity'] = df['Quantity'].fillna(df['Quantity'].mean())
df['Price'] = df['Price'].fillna(df['Price'].median())

df['Revenue'] = df['Quantity'] * df['Price']

Rename = df.rename(columns={'Price':'UnitPrice'})
Drope = df.drop(columns=['Orderdate'])

summary = df.groupby('Region').agg({
    'Revenue':['sum','mean'],
    'OrderID':['count']
})