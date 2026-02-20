# in broadcasting we will lwarn how adding or other thing happen b/w to arrays
# 1D example
import numpy as np
a = np.array([1,2,3,4])
print(a + 10)
b = np.array([10,20,30,40])
c = a+b
print(c)
d = np.array([
    [1,2,3,4],
    [4,5,6,7]
])
e = d + b
print(e)