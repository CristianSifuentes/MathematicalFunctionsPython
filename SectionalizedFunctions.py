import matplotlib.pyplot as plt   # librería para graficar
import numpy as np 



def H(x):
    Y = np.zeros(len(x))
    for idx,x in enumerate(x):
       if x>=0:
         Y[idx]=1
    return Y

N=100

x = np.linspace(-10,10, num=N)

y = H(x)

plt.plot(x,y)
print(plt.grid())       