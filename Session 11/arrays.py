import numpy as np
a = np.array([10, 20, 30, 40])
print(a.shape)
b = np.zeros((5,3))
print(b)
c = np.ones((10,28,28)) # its like example 10 items with 28 rows and 28 columns
#print(c)
# how to update a column or row & how to access perticular number
b[0][1] = 12
print((b), (b[0][1]))