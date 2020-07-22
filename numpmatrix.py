import numpy as np
x=[[1,2,3],[5,6,7],[8,9,10]]
y=((2,3,4),(6,7,8),(9,10,11))
a=np.array(x)
print(a)
b=np.array(y)
print(b)
print(a*b)
print(a.dot(b))