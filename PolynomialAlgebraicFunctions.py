import matplotlib.pyplot as plt   # librería para graficar
import numpy as np 

N = 100


def f(x):
  return (2*x**7)-(x**4)+(3*x**2)+4

x = np.linspace(-10,10, num=N)

y = f(x)

plt.plot(x,y)
print(plt.grid())            # librería para manejo de vectores y utilidades matemáticas