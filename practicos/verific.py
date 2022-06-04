import matplotlib.pyplot as plt
import numpy as np

# x = np.array(range(0,11))
# y = np.array([1.8, 3.5, 2.1, -1.0, -3.3, -2.7, 0.9, 3.3, 2.8, -0.1, -3.0])

def fun(x): return np.exp(x) 
def ajustelin(x): return 1.17 + 1.09 * x
def ajustecuad(x): return 1.17 + 1.09 * x + 0.5 * (x**2-1/3)

s = np.linspace(-1, 1, 600)
plt.plot(s, fun(s), label="Funcion")
plt.plot(s, ajustelin(s), label="Lineal")
plt.plot(s, ajustecuad(s), label="Cuad")
plt.legend()
plt.show()