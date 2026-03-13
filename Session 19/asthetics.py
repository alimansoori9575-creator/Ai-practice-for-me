import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Day" : [1,2,3,4,5],
    "Users" : [120,150,170,160,180],
    "Purchases" : [30,35,40,38,45]
}

df = pd.DataFrame(data)
#print(df)

# Markers are o, s, ^, x
plt.plot(df['Day'], df['Users'], linestyle='--', linewidth='2', marker='o', color='crimson', markerfacecolor="black", label='user') 
plt.plot(df['Day'], df['Purchases'], linestyle='--', linewidth='1', marker='o', color='gold', markerfacecolor="black", label='purchase') 
plt.grid(True)
plt.legend()
plt.text(3,170, "Peak day", fontsize=8, color="black") # To write text on mentioned area
plt.show()