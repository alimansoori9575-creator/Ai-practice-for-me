import pandas as pd

df = pd.read_csv("Sales_data.csv")
#print(df)

# detect missing data
print(df.isnull())
#count missing value per count
print(df.isnull().sum())
#to drop\remove null rows ------->  means drop missing values
df_clean = df.dropna()
print(df_clean)
# Drop only rows where selected column is missing ex:
df_clean2 = df.dropna(subset=["Discount", 'Price'])# u can select multiple
print(df_clean2)
# Drop columns with missing values
df_clean3 = df.dropna(axis=1)
print(df_clean3)
# to drop selected columns
df_clean0 = df.drop(['Price'],axis=1)
print(df_clean0)

