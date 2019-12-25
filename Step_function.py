import numpy as np
def func(x,T):
    y=np.where(x>=T,1,0)
    return y
x=np.array([[1,2,3,4,5,2,1,1]])
T=2
y=func(x,T)
print(y)