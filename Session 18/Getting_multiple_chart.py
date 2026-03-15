import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Day" : [1,2,3,4,5],
    "Users" : [120,150,170,160,180],
    "Purchases" : [30,35,40,38,45]
}

df = pd.DataFrame(data)
#print(df)

plt.figure(figsize=(10,4))# this is to manually give chart size like 10/4

plt.subplot(1, 2, 1) # this mean 1st row 2nd column and 1st position
plt.plot(df['Day'], df['Users']) 
plt.xlabel("Day")
plt.ylabel("Numbers of Users")
plt.title("App users over time")


plt.subplot(1, 2, 2)
plt.scatter(df['Users'], df['Purchases'])
plt.xlabel("Users")
plt.ylabel("Numbers of purchases")
plt.title("Users Vs Purchases")
plt.show()
