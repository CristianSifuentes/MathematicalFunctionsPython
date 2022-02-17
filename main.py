import matplotlib.pyplot as plt   # librería para graficar
import numpy as np 


N = 100

m = -1

b = 3

def f(x):
  return m*x+b

x = np.linspace(-10,10, num=N)

y = f(x)

fig, ax = plt.subplots()
ax.plot(x,y)
print(ax.grid())               # librería para manejo de vectores y utilidades matemáticas