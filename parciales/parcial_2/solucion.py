from typing import Iterable
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# EJ1
data = np.genfromtxt("./irma.csv", delimiter=",")
horas = data[:, 0]
longitud = data[:, 1]
latitud = data[:, 2]

# a
plt.plot(longitud, latitud, "o", label="Puntos (longitud, latitud) 1.a")
plt.legend()

# b
def plagrange(xs, ys):
    '''
    A partir de una lista de nodos y otra de sus imagenes, 
    usa el polinomio interpolante de Lagrange para construir un polinomio
    '''
    cnodos = len(xs)
    # Primero armo los polinomios basicos de lagrange

    def l(i, x):
        term = 1
        for j in range(0, cnodos):
            if(j != i):
                term *= (x-xs[j])/(xs[i]-xs[j])
        return term

    # Despues armamos la funcion a evaluar usando xs e ys

    def q(x):
        sum = 0
        for i in range(0, cnodos):
            sum += ys[i]*l(i, x)
        return sum

    return q

# Horas restantes
horas_inter = np.array([x for x in range(1, 24) if x not in horas])

# Longitud 
lin = np.linspace(0, 24, 200)
sp_long = interp1d(horas, longitud, kind="cubic")
lg_long = plagrange(horas, longitud)

fig, ax = plt.subplots()
fig.suptitle("Longitud")
ax.plot(horas, longitud, "o", label="Datos longitud")
ax.plot(horas_inter, sp_long(horas_inter), "o", label="Inter spline")
ax.plot(horas_inter, lg_long(horas_inter), "o", label="Inter Lagrange")

ax.legend()

# Latitud

lg_lat = interp1d(horas, latitud, kind="cubic")
sp_lat = plagrange(horas, latitud)

fig, ax = plt.subplots()
fig.suptitle("Latitud")
ax.plot(horas, latitud, "o", label="Datos latitud")
ax.plot(horas_inter, sp_lat(horas_inter), "o", label="Inter spline")
ax.plot(horas_inter, lg_lat(horas_inter), "o", label="Inter Lagrange")

ax.legend()


# EJ2
x = [0, 1.5, 2, 2.9, 4, 5.6, 6, 7.1, 8.05, 9.2, 10, 11.3, 12]
y = [0.1, 0.2, 1, 0.56, 1.5, 2, 2.3, 1.3, 0.8, 0.6, 0.4, 0.3, 0.2]
# a)
fig, ax = plt.subplots()
ax.plot(x, y, "o", label="Puntos discretos 2.a")
ax.legend()

# b)
def trapecio_adaptativo(x: Iterable, y: Iterable):
    if(not all(x[i]<x[i+1] for i in range(0, len(x)-1))):
        raise Exception("Los puntos se deben dar ordenados")
    if(len(x) != len(y)):
        raise Exception("Ambas listas de puntos deben tener la misma dimensión.") 
    if(len(x) < 2):
        raise Exception("Se requieren al menos dos puntos para el trapecio adaptativo.") 
    sum = 0

    # Calculo regla del trapecio en cada subintervalo
    for i in range(0, len(x)-1):
        sum += (x[i+1] - x[i])/2 * (y[i] + y[i+1])
        pass
    return sum


# c)
i = trapecio_adaptativo(x, y)
print(f"Metros cubicos a remover: {10*i}") # Area estimada bajo la curva * 10 metros de profundidad del terreno

plt.show()