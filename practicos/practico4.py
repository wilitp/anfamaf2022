from datetime import date
import numpy as np
from numpy.random import randn
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
xs = np.linspace(0, 10, 20)
ys = fun1c(xs)
ys = ys + 3*randn(len(ys))

# ajuste = ajuste_lineal(x, yd)
ajuste = np.poly1d(np.polyfit(xs, ys, 1)) # polyfit devuelve los coeficientes del polinomio, con poly1d obtenemos un polinomio que podemos evaluar(callable)
# plt.plot(xs, ys, "o", label="Datos dispersados")
# plt.plot(x, ajuste(x), label="Ajuste")
# plt.plot(x, fun1c(x), label="Funcion")

# 2

def func2a(x):
    return np.arcsin(x)

# a
# Genero los datos
x = np.linspace(0, 1, 50)
x_graph = np.linspace(0, 1, 200)
y = func2a(x)
ys = y + randn(len(y))

# for n in range(1,6):
#     ajuste = np.poly1d(np.polyfit(x, ys, n))
#     # Imagen de x en ajuste
#     ya = ajuste(x)
#     residuo = sum(np.abs(y-ya))
#     print(f"Residuo grado {n}: {residuo}")
#     plt.plot(x_graph, ajuste(x_graph), label=f"Ajuste grado {n}")


# plt.plot(x, ys, "o", label="Datos")
# plt.plot(x_graph, func2a(x_graph), label="Arcsin")


# def func2b():
#     return np.cos(x)


# b

def func2b(x):
    return np.cos(x)

# Genero los datos
x = np.linspace(0, 4*np.pi, 50)
x_graph = np.linspace(0, 4*np.pi, 200)
y = func2b(x)
ys = y + randn(len(y))

# for n in range(1,6):
#     ajuste = np.poly1d(np.polyfit(x, ys, n))
#     # Imagen de x en ajuste
#     ya = ajuste(x)
#     residuo = sum(np.abs(y-ya))
#     print(f"Residuo grado {n}: {residuo}")
#     plt.plot(x_graph, ajuste(x_graph), label=f"Ajuste grado {n}")


# plt.plot(x, ys, "o", label="Datos")
# plt.plot(x_graph, func2b(x_graph), label="Cos")



# plt.legend()
# plt.show()


# 3
# a
datos = np.loadtxt("../datos/datos3a.dat")
x = datos[0]
y = datos[1]

x = x[~np.isnan(y)]
y = x[~np.isnan(y)]

# f(x) ~ C * x**A
# ln(f(x)) ~ ln(C) + A*ln(x)
# yn ~ cn + an*xn

yn = np.log(y)
xn = np.log(x)
a, cn = np.polyfit(xn, yn, 1)
c = np.exp(cn)

def ajuste(x): return c*x**a

# plt.plot(x, y, "o", label="Datos")
# plt.plot(x, ajuste(x), label="Ajuste")
# plt.legend()
# plt.show()

# b
datosb = np.loadtxt("../datos/datos3b.dat")

x = datos[0]
y = datos[1]

x = x[~np.isnan(y)]
y = x[~np.isnan(y)]

# y ~ x / A * x + B
# x/y ~ A * x + B

a, b = np.polyfit(x, x/y, 1)

def ajuste(x): return x/(a*x+b)

# plt.plot(x, y, "o", label="Datos")
# plt.plot(x, ajuste(x), label="Ajuste")
# plt.legend()
# plt.show()

# 4

datos = np.loadtxt("../datos/covid_italia.csv",delimiter=",", dtype=str)
dates = datos[:, 0].astype(date)
cases = datos[:, 1].astype(int)

# No puedo operar sobre fechas, asi que para hacer el ajuste enumero los dias
x = np.array(range(1, len(dates)+1))

# y ~ a * e**(b*x)
# ln(y) ~ ln(a) + b*x

y = cases
yn = np.log(y)
b, an = np.polyfit(x, yn, deg=1)
a = np.exp(an)

def ajuste(x): return a * np.exp(b*x)

# plt.plot(x, cases, "o", label="Casos Covid Italia")
# plt.plot(x, ajuste(x), label="Ajuste")
# plt.legend()


# plt.show()
