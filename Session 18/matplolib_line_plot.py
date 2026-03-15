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
plt.plot(df['Day'], df['Users'])
# to label x & y 
plt.xlabel("Day")
plt.ylabel("Numbers of Users")
# to give title
plt.title("App users over time")
plt.show()