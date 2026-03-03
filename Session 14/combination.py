import pandas as pd

df = pd.read_csv("employee.csv")

# give me a table which has students with salary 80000 above 
# show only name, role and salary in desending order

# first step by step
result_1 = df[(df['role'] == 'student') & (df['salary'] > 80000)]
result_2 = result_1[['name','role','salary']]
result_3 = result_2.sort_values('salary', ascending=False)
#print(result_3)

#in one go
result = (
    df[(df['role'] == 'student') & (df['salary'] > 80000)]
    [['name','role','salary']]
    .sort_values('salary', ascending=False)
    )
print(result)