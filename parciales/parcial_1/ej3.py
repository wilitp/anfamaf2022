from utils import rbisec
from ej1 import serie_seno

# Raiz de 2 a 4
hx, _ = rbisec(serie_seno, [2,4], 1e-5, 100)
print(f"La primera raiz positiva se estima en {hx[-1]}")

# 4 a 6
hx, _ = rbisec(serie_seno, [4,6], 1e-5, 100)
print(f"La segunda raiz positiva se estima en {hx[-1]}")