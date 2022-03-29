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

![Alt text](/Images/TrigonometricFunctions.png?raw=true "TrigonometricFunctions.png")


```python
def f(x):
  return np.cos(x)

y = f(x)

plt.plot(x,y)
```

![Alt text](/Images/TrigonometricFunctionsGrap.png?raw=true "Trigonometric Functions Grap.png")

## Exponential function

![Alt text](/Images/ExponentialFunctions.png?raw=true "Exponential Functions.png")

```python
def f(x):
  return np.exp(x)

y=f(x)

plt.plot(x,y)
```
![Alt text](/Images/ExponentialFunctionsGrap.png?raw=true "Exponential Functions Grap.png")

## Logarithm Function

![Alt text](/Images/LogarithmFunction.png?raw=true "LogarithmFunction.png")

```python
def f(x):
  return np.log2(x)

x = np.linspace(0.001,256, num=1000)
plt.plot(x,f(x))
```

![Alt text](/Images/LogarithmFunctionGrap.png?raw=true "LogarithmFunction Grap.png")

## Sectioned Function

![Alt text](/Images/SectionedFunction.png?raw=true "Sectioned Function.png")

```python
def H(x):
  Y = np.zeros(len(x))
  for idx,x in enumerate(x):
    if x>=0:
      Y[idx]=1
  return Y
    

N=1000

x = np.linspace(-10,10, num=N)

y = H(x)

plt.plot(x,y)
```


![Alt text](/Images/SectionedFunctionGrap.png?raw=true "Sectioned Function Grap.png")