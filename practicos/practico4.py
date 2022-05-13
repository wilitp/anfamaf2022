import numpy as np
from numpy.random import rand, randn
from matplotlib import pyplot as plt
 
# 1 a,b

# Datos nose
datos = np.loadtxt("../datos/datos1a.dat")
# Datos tristes de cuando nos asamos
# datos = np.loadtxt("../datos/datos_aeroCBA.dat")
x = datos[:,0]
y = datos[:,1]
mask = ~np.isnan(y)
x = x[mask]
y = y[mask]
def ajuste_lineal(x,y):
    m = len(x)
    sum_x = np.dot(x, np.ones(m))
    sum_x_cuadrado = sum(x**2)
    sum_xy = np.dot(x, y)
    sum_y = np.dot(y, np.ones(m))
    cociente = ((m*sum_x_cuadrado) - (sum_x**2))
    b = (sum_x_cuadrado*sum_y - sum_xy*sum_x)/cociente
    a = (m*sum_xy - sum_x * sum_y)/cociente
    return lambda h:(a*h+b)
ajuste = ajuste_lineal(x,y)

# plt.plot(x, y, "o")
# plt.plot(x, ajuste(x))

# 1 c

def fun1c(x): return 3/4 * x - 1/2 

x = np.linspace(0, 10)
y = fun1c(x)
yd = y + 3*randn(len(y))
ajuste = ajuste_lineal(x, yd)
plt.plot(x, yd, "o", label="Datos dispersados")
plt.plot(x, ajuste(x), label="Ajuste")
plt.plot(x, y, label="Funcion")
plt.legend()
plt.show()