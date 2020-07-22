import numpy as np
x=[10,20,30,30]
A=np.array(x)
amean=A.mean()
print(amean)
print()
var=A-amean
print(var)
v=var**2
print(v)
x=v.sum()
print(x)
print(x/A.size)
print('\t',(((A-(A.mean()))**2).sum())/(A.size))
