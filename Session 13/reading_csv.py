import pandas as pd

# to read csv or other file
df = pd.read_csv(r"C:\Users\91917\Desktop\Sessions\Ai-practice-for-me\Session 13\employe.csv")
#print(df)
# to inspect the data 
val = df.head(6)# its to inspect column and data format by default it gives you first 5 but u can add no. accourding to need
#print(val)

val2 = df.tail()#it to inspect last 
#print(val2)

val3 = df.iloc[1:6]# it to inspect manually
#print(val3)

info = df.info()# it give column no., datatype, non nul count
#print(info)

desc = df.describe()# it will describe some basic about table
print(desc)