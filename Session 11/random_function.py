import numpy as np
print(np.random.rand(5))# it will pick numbers b/w 0 to 1
print(np.random.randn(5))# it will pick any no. even nagative values but mostly near 0
# random integer
print(np.random.randint(0,10,(5)))
print(np.random.randint(0,10,(5,2)))

### seed will hold same value ex:
np.random.seed(42)# you can put any value in ()
print(np.random.rand(5))