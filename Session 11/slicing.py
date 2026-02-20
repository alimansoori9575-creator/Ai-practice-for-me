import numpy as np
# slicing in 1D
a = np.array([10,20,30,40])
print(a[1:3])
# slicing in 2D
b = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(b[1:3, 0:2]) # first is for row & second for column