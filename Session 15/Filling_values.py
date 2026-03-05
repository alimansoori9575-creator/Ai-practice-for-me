import pandas as pd

df = pd.read_csv("Sales_data.csv")
#print(df)
# how to fill null values
df['Discount'] = df['Discount'].fillna(0)
print(df)

# If all values in column are near then you can use mean
df['Price'] = df['Price'].fillna(df['Price'].mean())
print(df)
# if valuse are not near or has one or two outliners so use median
df['Price'] = df['Price'].fillna(df['Price'].median())
print(df)