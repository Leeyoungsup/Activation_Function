import numpy as np
def func(x):
    y=(1-np.exp(-x))/(1+np.exp(-x))
    return y
x=np.array([[-1,-2,3,-4,5,-2,1,1]])
y=func(x)
print(y)