import numpy as np
a = np.array([1,2,3,4,5,6])
b = a[1:5]
print(b)
b[3] = 999
print(a) # you can overwrite origenal using slice
# to prevent that u can use .copy it creates new copy
c = np.array([10,20,30,40])
d = c[1:3].copy()
d[1] = 999
print(d)
print(c)