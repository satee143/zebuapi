import numpy as np
a=np.arange(12).reshape(3,4)
print(a)
print(a[2,1:3])
print(a[1:,1:3])
print(a[:,1,])