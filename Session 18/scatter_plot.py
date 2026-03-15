import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Day" : [1,2,3,4,5],
    "Users" : [120,150,170,160,180],
    "Purchases" : [30,35,40,38,45]
}

df = pd.DataFrame(data)
#print(df)

# to get chart
plt.scatter(df['Users'], df['Purchases'])
# to label x & y 
plt.xlabel("Users")
plt.ylabel("Numbers of purchases")
# to give title
plt.title("Users Vs Purchases")
plt.show()

# Use plot.figure() when you want more then one chart individually