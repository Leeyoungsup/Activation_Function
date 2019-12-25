import numpy as np
def func(x,T):
    y=np.where(x>=T,x,0)
    return y
x=np.array([[-1,-2,3,-4,5,-2,1,1]])
T=0
y=func(x,T)
print(y)