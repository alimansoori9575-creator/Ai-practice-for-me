import pandas as pd

data = {
    "Name": ["Ali", "Zaid", "Danish"],
    "Math": [87, 85, 94],
    "Science": [89, 85, 90]
}
df = pd.DataFrame(data)
print(df)
print(df["Name"])
print(df[['Name','Math','Science']])