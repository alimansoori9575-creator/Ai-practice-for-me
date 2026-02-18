numbers = [1, 2, 3, 4, 5]

squered = []
for i in numbers:
    squered.append(i * 2)
print(squered)
### Now using NumPy
import numpy as np
num_np =  np.array([1, 2, 3, 4])
squered_np = num_np * 2
print(squered_np)