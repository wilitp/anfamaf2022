from typing import Iterable
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# 1

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
    x = a
    for _ in range(1, N):
        x = x+h
        sx += fun(x)
    return (sx0 + 2*sx) * h / 2

def pm(fun, a: float, b: float, N: int):
    h = (b-a)/N
    sx = 0
    x = a
    for _ in range(0, N+1, 2):
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
# 2

f = lambda x : np.exp(-x)
# for n in [4, 10, 20]:
#     print(f"\n\nCon {n} subintervalos")
#     print(f"Trapecio: {intenumcomp(f, 0, 1, n, 'trapecio')}")
#     print(f"Simpson: {intenumcomp(f, 0, 1, n, 'simpson')}")
#     print(f"Punto medio: {intenumcomp(f, 0, 1, n, 'pm')}")

# 3

def senintaux(x):
    return intenumcomp(np.cos, 0, x, int(np.ceil(x*10)), "trapecio") # Cantidad de subintervalos tal que sean <= 0.1

def senint(x: Iterable[float]): 
    return list(map(senintaux, x))

# x = np.arange(0, 2*np.pi, 0.5) 
# plt.plot(x, np.sin(x), label="Seno")
# plt.plot(x, senint(x), "o", label="Integral numérica desde 0 a ese punto")

# 4
# Aplicar las reglas con una cantidad n y luego con n+1.
# Si la diferencia es menor a la tolerancia entonces devuelvo la ultima

# 5
# print(f"a: {quad(lambda x:np.exp(-x**2), -np.inf, np.inf)}")
# print(f"b: {quad(lambda x:x**2*np.log(x+np.sqrt(x**2+1)), 0, 2)}")

# 6
def pendulo(l, angDeg):
    angRad = angDeg*np.pi/180
    def aux(x):
        return 1/(1 - np.sin(angRad/2)**2 * np.sin(x)**2)
    
    integral, _ = quad(aux, 0, np.pi/2)
    return 4*np.sqrt(l/9.8)*integral

def S(f, a, b):
    return (b-a)/6 * (f(a) + 4*f((a+b)/2) + f(b))

# 7
def quadadapt(f, I, tol):
    a, b = I
    c = (a+b)/2
    q = S(f, a,b)
    q1 = S(f, a,c)
    q2 = S(f, c,b)
    if q-q1-q2 < 15*tol:
        return q1 + q2
    else:
        return quadadapt(f, (a,c), tol/2) + quadadapt(f, (c, b), tol/2)

def f(x): return x * np.e**(-x**2)
print(quadadapt(f, (0, 1), 1e-5))
print(intenumcomp(f, 0, 1, 8, "simpson"))
# print()

plt.show()