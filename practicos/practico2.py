from math import cos, fabs, inf, sqrt, tan, exp
import matplotlib.pyplot as plt
import numpy as np

def newej(n):
    print("\n\n")
    print(f"Ej {n} --------------------------------------------------------]")
    print("\n")


def rbisec(f, I, err, mit):
    '''
    # 1 Escribir una funcion que implemente el metodo de biseccion
    # Takes a function and the two values that bracket the root
    '''
    # Brackets
    b1 = I[0]
    b2 = I[1]
    hx = [(b1+b2)/2]
    hy = [f(hx[0])]
    k = 0
    if fabs(f(hx[0])) < err:
        return (hx, hy)

    while fabs(f(hx[k])) >= err and k+1 < mit and f(hx[k]) != 0:

        if diff_sign(f(b1), f(hx[k])):
            b2 = hx[k]
        else:
            b1 = hx[k]

        # Nuevo punto medio
        k += 1
        hx += [(b1+b2)/2]
        hy += [f(hx[k])]

    return (hx, hy)


def diff_sign(x, y):
    return x > 0 and y < 0 or x < 0 and y > 0


# 2 Usar rbisec para:
newej(2)

fig, ax = plt.subplots()

# a) encontrar la menor solucino positiva de la ecuacion 2.x = tan(x) con un error menor a 10**-5 en menos de 100 iteraciones. Cuantas iteraciones son necesarias cuando comenzamos con el intervalo [0.8, 1.4]/ Usar la siguiente sintaxis:


def fun_lab2ej2a(x):
    return 2*x - tan(x)


hx, hy = rbisec(fun_lab2ej2a, [0.8, 1.4], 1e-5, 20)

x = np.linspace(0, 2, 200)
ax.plot(hx, hy, '*', label="Estimaciones ej2a")
ax.plot(x, 2*x - np.tan(x), label="Fun ej2a")

print(
    f"2.a: Hicieron falta {len(hx)} iteraciones, para encontrar la aproximacion {hx[-1]}")


# b) Encontrar una aproximacion a raiz de tres con un error menor a 10**-5, para esto considere la funcion x -> x**2 -3

def fun_lab2ej2b(x):
    return x**2 - 3


hx, hy = rbisec(fun_lab2ej2b, [1.4, 2], 1e-5, 20)
print(
    f"2.b: Usando el intervalo [1.4, 2], hicieron falta {len(hx)} iteraciones para aproximar raiz de tres con un error menor a 10**-5: {hx[-1]} al cuadrado es {hx[-1]**2}")

ax.plot(hx, hy, '*', label="Estimaciones ej2b")
ax.plot(x, x**2 - 3, label="Fun ej2b")
ax.set_xlabel("Eje x")
ax.set_ylabel("Eje y")
ax.legend()
plt.show()

# 3. Escribir una funion que implemente el metodo de Newton para hallar una raiz de f : R -> R partiendo de un punto inicial x0.
# La funcion debe llamarse `rnewton`, y tener como entrada (fun, x0, err, mit) donde fun es una funcion que dado x retorna f(x) y f'(x)
newej(3)

# 3 es


def rnewton(fun, x0, err, mit):
    hx = []
    hf = []
    x_1 = x0

    for k in range(0, mit):
        x, xprim = fun(x_1)
        xk = x_1 - x/xprim
        hx += [xk]
        hf += [fun(xk)[0]]
        if fabs(xk-x_1)/fabs(xk) < err or fabs(fun(xk)[0]) < err or k > mit:
            break
        x_1 = xk

    return (hx, hf)


def raiz_cubica(a):
    '''
    Aproxima raiz cubica de `a` usando el metodo de newton
    '''

    def f(x): return x**3 - a
    def fprima(x): return 3*x**2

    def fun(x): return (f(x), fprima(x))

    x0 = a/3
    xh, _ = rnewton(fun, x0, 1e-6, 1000)

    return xh[-1]


a = 9
print(
    f"Una aproximacion de la raiz cubica de {a} es {raiz_cubica(a)}, cuyo cubo es {raiz_cubica(a)**3}")

# 5
newej(5)


def ripf(fun, x0, err, mit):
    k: int = 0
    # xh almacena la estimacion para cada iteracion
    xh = [x0]
    x = x0+err+1

    while k < mit:
        x = fun(x0)
        k += 1
        xh = xh + [x]
        if fabs(x0-x) < err:
            break
        x0 = x

    return xh


# 6
newej(6)


def fun_lab2ej6(x): return 2**(x-1)
# La derivada nos da 2**(x-1) * ln(2)
# Para cualquier x < 1, esta derivada es < 1
# Ademas, la funcion es exponencial, por lo que tiende a 0(+) cuando x tiende a -Inf.
# Concluyo entonces que la funcion converge con cualquier x0 en (-Inf,1)


hx = ripf(fun_lab2ej6, 2.0000001, 1e-5, 100)
lst = hx[-1]
print(
    f"Una aproximacion de un punto fijo de 2x=2**x con x0(1.7) en el intervalo [1,2] es {hx[-1]}, f({lst})={fun_lab2ej6(lst)}")
print("Concluyo que el metodo converge con x0 en (-Inf, 1)")

# 7
newej(7)


def fun_lab2ej7bisec(x):
    # funcion de la que buscar una raiz
    def ec(y): return y - exp(-((1-x*y)**2))

    hy, _ = rbisec(ec, [0, 2], 1e-5, 200)
    return hy[-1]


print(f"u(0.7)={fun_lab2ej7bisec(0.7)}, segun biseccion")


def fun_lab2ej7newton(x):
    # funcion de la que buscar una raiz
    def ec(y): return y - exp(-((1-x*y)**2))
    def ecprim(y): return 1 - 2*exp(-(1-x*y)**2)*(x-(x**2)*y)
    def f(y): return (ec(y), ecprim(y))

    # Al despejar la ecuacion y = e**(-(1-xy)**2),
    # Obtenemos ln y = -((1-xy)**2), osea que ln y<0
    # Por lo tanto y esta entre 0 y 1.
    # Uso entonces y0 = 0.5

    y0 = 0.5
    hy, _ = rnewton(f, y0, 1e-5, 200)
    return hy[-1]


print(f"u(0.7)={fun_lab2ej7newton(0.7)}, segun Newton")


def fun_lab2ej7ipf(x):
    # funcion de la que buscar una raiz
    def ec(y): return exp(-((1-x*y)**2))

    # Al despejar la ecuacion y = e**(-(1-xy)**2),
    # Obtenemos ln y = -((1-xy)**2), osea que ln y<0
    # Por lo tanto y esta entre 0 y 1.
    # Uso entonces y0 = 0.5

    y0 = 0.5
    hy = ripf(ec, y0, 1e-5, 200)
    return hy[-1]


print(f"u(0.7)={fun_lab2ej7ipf(0.7)}, segun Iteracion de punto fijo")

newej(8)
# Encontrar el minimo de tan(x)/x**2 en el intervalo (0, pi/2) usando el metodo de Newton
# para encontrar una raiz de su derivada


def derivadafea(x): return (x+x*tan(x)**2-2*tan(x))/x**3


def derivadafea2(x): return 2*(x**2*(1/cos(x))**2 *
                               tan(x)-2*x*(1/cos(x))**2+3*tan(x))/x**4


def ffea(x): return (derivadafea(x), derivadafea2(x))


hx, hf = rnewton(ffea, 1.5, 1e-5, 200)
print(hf)

print(
    f"El minimo de la funcion entre 0 y medio pi es {hx[-1]}, segun el metodo de Newton")


newej(9)


# Funcion que da 0 cuando el diametro del las aspas es el necesario para
# tener un output de 500W
def fun_lab2ej9(d): return (d**2)*(296.29629629629636) - 500
def fun_lab2ej9prim(d): return 2*d*(296.29629629629636)
def f(x): return (fun_lab2ej9(x), fun_lab2ej9prim(x))


hx, _ = rnewton(f, 1.3, 1e-5, 200)

print(
    f"Es necesario una velocidad de {hx[-1]} para tener 500W de output segun el metodo de Newton")
