import matplotlib.pyplot as plt   # librería para graficar
import numpy as np 


def f(x):
      return np.log2(x)

x = np.linspace(0.001,256, num=1000)
plt.plot(x,f(x))
print(plt.grid())   