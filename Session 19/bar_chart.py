import matplotlib.pyplot as plt

modles = ["Modal A", "Modal B", "Modal C"]
sales = [40, 45, 38]

plt.bar(modles, sales)
plt.xlabel("Model")
plt.ylabel("Sales")
plt.title("Modles comparison")

plt.show()