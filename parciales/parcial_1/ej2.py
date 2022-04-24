import matplotlib.pyplot as plt
from ej1 import serie_seno
import math

# Lista y su imagen
lower = 0
upper = 6.4
length = math.ceil((upper-lower)/0.1)
xs = [lower + x*(upper-lower)/length for x in range(length)]
ys = list(map(serie_seno, xs))

# Grafico
fig, ax = plt.subplots()
ax.plot(xs, ys, "*", label="Taylor seno 5 terminos centrado en 0")
ax.legend()
plt.show()
