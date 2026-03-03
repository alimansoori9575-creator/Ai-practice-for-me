import pandas as pd

df = pd.read_csv("employee.csv")

x = df.sort_values('salary')
#print(x)
# to get desending
y = df.sort_values('salary', ascending=False)
#print(y)

# sorting by multiple column

z = df.sort_values(['salary','age'])
# yaha per esa he pehle salary ke basis par sort kro agar salary barabar hai to age dekho
#print(z)

w = df.sort_values(['salary','age'], ascending=[True, False])
print(w)

v = df.sort_index