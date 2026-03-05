import pandas as pd
df = pd.read_csv("Sales_data.csv")
#print(df)

## how groupby works

df["Revenue"] = df['Quantity'] * df['Price']# this will create new column named revenue
print(df)

# What is the total revenue per region
df_rev = df.groupby('Region')['Revenue'].sum()
print(df_rev)

# Which reagion earn the most
df_rev_sort = df.groupby('Region')['Revenue'].sum().sort_values(ascending=False)
print(df_rev_sort)

# Average revenue per region
df_rev_avg = df.groupby('Region')['Revenue'].mean()
print(df_rev_avg)