from math import fabs, inf, sqrt, tan


def last(arr):
    return arr[len(arr) - 1]


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

# a) encontrar la menor solucino positiva de la ecuacion 2.x = tan(x) con un error menor a 10**-5 en menos de 100 iteraciones. Cuantas iteraciones son necesarias cuando comenzamos con el intervalo [0.8, 1.4]/ Usar la siguiente sintaxis:
def fun_lab2ej2a(x):
    return 2*x - tan(x)


hx, hy = rbisec(fun_lab2ej2a, [0.8, 1.4], 1e-5, 100)

print(f"2.a: Hicieron falta {len(hx)} iteraciones")


# b) Encontrar una aproximacion a raiz de tres con un error menor a 10**-5, para esto considere la funcion x -> x**2 -3

def fun_lab2ej2b(x):
    return x**2 - 3


hx, hy = rbisec(fun_lab2ej2b, [1.4, 2], 1e-5, 20)
print(
    f"2.b: Usando el intervalo [1.4, 2], hicieron falta {len(hx)} iteraciones para aproximar raiz de tres con un error menor a 10**-5: {hx[len(hx)-1]}**2={hx[len(hx)-1]**2}")

# c) Graficar conjuntamente f y los pares (x_k, f(x_k)) para las dos funciones anteriores y
# con al menos dos intervalos iniciales distintos para cada una.

# 3. Escribir una funion que implemente el metodo de Newton para hallar una raiz de f : R -> R partiendo de un punto inicial x0.
# La funcion debe llamarse `rnewton`, y tener como entrada (fun, x0, err, mit) donde fun es una funcion que dado x retorna f(x) y f'(x)


# 3 es
def rnewton(fun, x0, err, mit):
    hx = []
    hf = []
    x_1 = x0

    for k in range(0, mit):
        x, xprim = fun(x_1)
        xk = x_1 - x/xprim
        hx += [xk]
        hf += [fun(x0)[0]]
        if fabs(xk-x_1)/fabs(xk) < err or fabs(fun(xk)[0]) < err or k > mit:
            break
        x_1 = xk

    print(hx)
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

    return last(xh)


a = 9
print(
    f"Una aproximacion de la raiz cubica de {a} es {raiz_cubica(a)}, cuyo cubo es {raiz_cubica(a)**3}")

# 5


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


def fun_lab2ej6(x): return 2**(x-1)


hx = ripf(fun_lab2ej6, 0.5, 1e-5, 100)
lst = hx[-1]
print(
    f"Una aproximacion de un punto fijo de 2x=2**x en el intervalo [0,1] es {last(hx)}, f({lst})={fun_lab2ej6(lst)}")

hx = ripf(fun_lab2ej6, 1.3, 1e-5, 100)
lst = hx[-1]
print(
    f"Una aproximacion de un punto fijo de 2x=2**x en el intervalo [1,2] es {last(hx)}, f({lst})={fun_lab2ej6(lst)}")

# 7
