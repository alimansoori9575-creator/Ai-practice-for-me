import pandas as pd

df = pd.read_csv("employee.csv")
#print(df)
x = df[df['age'] > 22]
#print(x)

y = df[df['role'] == 'student']
#print(y)

z = df[(df['tdc_no'] < 100) & (df['salary'] > 80000)]
#print(z)

# | is for i want both
w = df[(df['role'] == 'student') | (df['role'] == 'husband')]
#print(w)

# ~ is for what we don't want

v = df[~(df['class'] == 15)]# we can also use != this
print(v)