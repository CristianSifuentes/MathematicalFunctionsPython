import matplotlib.pyplot as plt   # librería para graficar
import numpy as np 

N = 100


def f(x):
      return np.tan(x)
  
x = np.linspace(-10,10, num=N)


def f(x):
      return np.exp(x)

y=f(x)

plt.plot(x,y)
print(plt.grid())            # librería para manejo de vectores y utilidades matemáticas
