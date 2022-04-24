from ej4 import rsteffensen
from ej1 import serie_seno

# Busco las raices positivas de serie_seno con x0=3
xh, _ = rsteffensen(serie_seno, 3, 1e-5, 100)
print(f"Primera raiz estimada en {xh[-1]}. Hicieron falta {len(xh)} iteraciones")

# Busco las raices positivas de serie_seno con x0=6
xh, _ = rsteffensen(serie_seno, 6, 1e-5, 100)
print(f"Segunda raiz estimada en {xh[-1]}. Hicieron falta {len(xh)} iteraciones")

# Busco las raices positivas de serie_seno con x0=4.5
xh, hf = rsteffensen(serie_seno, 4.5, 1e-10, 100)
print(f"Al usar x0=4.5, el metodo obtiene {xh[-1]}, cuya imagen es {hf[-1]}. Hicieron falta {len(xh)} iteraciones")

# RTAs:
# Al usar x0=-4.5

# El metodo devuelve un número alrededor de -8 como última estimacion, luego de 100 iteraciones.
# El metodo tambien devuelve un número alrededor de -8 como última estimacion, luego de 3 iteraciones.
# Esto se debe a que la diferencia entre estimaciones consecutivas se hace pequeña rapidamente.

# Podriamos obtener un resultado cercano con menos iteraciones si usaramos la diferencia entre las ultimas 2 estimaciones 
# como criterio de parada