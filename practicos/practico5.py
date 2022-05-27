import numpy as np
import matplotlib.pyplot as plt

def simp(fun, a: float, b: float, N: int):
    # Este algoritmo aplica la regla de simpson cada 2 subintervalos
    # por ende N aplicaciones => n subintervalos
    n = 2 * N
    h = (b-a)/n
    sx0 = fun(a) + fun(b)
    sx1 = 0
    sx2 = 0
    x = a
    for j in range(1, n):
        x = x + h
        if j%2==0:
            sx2 += fun(x)
        else:
            sx1 += fun(x)
    return (sx0 + 2*sx2 + 4*sx1) * h / 3

def trap(fun, a: float, b: float, N: int):
    h = (b-a)/N
    sx0 = fun(a) + fun(b)
    sx = 0
    x = 0
    for j in range(1, N):
        x = x+h
        sx += fun(x)
    return sx0 + 2*sx

def pm(fun, a: float, b: float, N: int):
    h = (b-a)/N
    sx = 0
    x = 0
    for j in range(0, N+1, 2):
        x += 2*h
        sx += fun(x)
    return 2*h*sx



def intenumcomp(fun, a: float, b: float, N: int, regla: str):
   reglas = {
       "trapecio": trap,
       "pm": pm,
       "simpson": simp
   }
   return reglas[regla](fun, a, b, N)



plt.show()