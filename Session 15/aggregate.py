import pandas as pd

df = pd.read_csv("Sales_data.csv")
#print(df)

df['Revenue'] = df['Quantity'] * df['Price']

# Average revenue per region
df_avg = df.groupby('Region')['Revenue'].mean()
print(df_avg)

# How many orders per region
df_reve = df.groupby('Region')['OrderID'].count()# count remove null value, u can use .size() instead 
print(df_reve)
# using size
df_rev1 = df.groupby('Region').size()
print(df_rev1)

# show sum, mean, count altogether
df_rev2 = df.groupby('Region')['Revenue'].agg(['sum','mean','count'])
print(df_rev2)

# revenue only on sum and mean and count on oderID
df_group = df.groupby("Region").agg({
    "Revenue": ["sum","mean"],
    "OrderID": "count"
})
print(df_group)

