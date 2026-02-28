import pandas as pd

data = {
    "Name": ["Ali", "Zaid", "Alice"],
    "Age": [21, 20, 16],
    "Salary": [2500, 1000, 100]
}
df = pd.DataFrame(data)
print(df)