# Mathematical Functions Python

## Description

This is a repository where I write about mathematical functions using and coding some examples in python, where main objective is show so me differences into them.

I wrote this repository because in the future I want come here and remember easily all highlight about mathematical functions, some differences and share all information getting in a platzi course about "Course on Mathematical Functions for Data Science and Artificial Intelligence"

## Table of Contents (Optional)

Algebraic functions.

   * [Algebraic functions
](#algebraic-functions)
      * [Linear Functions](#linear-functions)
      * [Polynomial Functions](#polynomial-functions)
   * [Transcendent functions
](#transcendent-functions)
      * [Trigonometric Functions](#trigonometric-functions)
      * [Exponential function](#exponential-function)
      * [Logarithm function](#logarithm-function)
   * [Sectioned function
](#sectioned-function)




## Linear Functions

![Alt text](/Images/LinearFunction.png?raw=true "Linear Function.png")


```python
N = 100

m = -1

b = 3

def f(x):
  return m*x+b

x = np.linspace(-10,10, num=N)

y = f(x)

fig, ax = plt.subplots()
ax.plot(x,y)
ax.grid()

```


## Polynomial Functions

![Alt text](/Images/PolynomialFunctions.png?raw=true "Polynomial Functions.png")


```python
def f(x):
  return x**7

y = f(x)

plt.plot(x,y)
plt.grid()

```

![Alt text](/Images/PolynomialFunctionsGrap.png?raw=true "Polynomial Functions Grap.png")

## Trigonometric functions

Algunos ejemplos son las funciones $cos(x)$, $sen(x)$ y $tan(x)$

## Exponential function

Tienen la forma de $$f(x)=a^x$$ donde la base $a$ es una constante positiva. Un gran ejemplo de una función exponencial es usando la base como el número de euler:

$$f(x)=e^x$$

## Logarithm Function

El logaritmo está definido por la **relación**:

$$log_{b}(x) = n \Longleftrightarrow x=b^n$$

donde:

*$b$ es la base.
*$n$ es el exponente al que está elevado la base.
*$x$ es el resultado de elevar la base $b$ al exponente $n$

**Ejemplo:**

Teniendo b=2 y n=8, entonces:

$$2^8=256$$

Por lo que $x=256$. Calculando el logaritmo base 2 de $x$ es:

$$log_{2}(256) = 8$$

## Sectioned Function

Son funciones que tienen diferentes valores definidos por un intervalo. Por ejemplo la función escalón de Heaviside:

$$
H(x) =
     \begin{cases}
        0, &\quad \text{para, } x < 0 \\
        1,  &\quad\text{para. } x \ge 0 \\
     \end{cases}
$$

$x_{n}$
$$\cos\bar{\phi}_k Q_{j,k+1,t} + Q_{j,k+1,x}+ \frac{\sin^2\bar{\phi}_k}{T\cos\bar{\phi}_k} Q_{j,k+1} = -\cos\phi_j Q_{j,k,t} + Q_{j,k,y}-\frac{\sin^2\phi_j}{T\cos\phi_j} Q_{j,k}$$

