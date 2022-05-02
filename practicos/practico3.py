from math import cos, fabs, pi
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from numpy import arange, linspace, loadtxt, isnan, asarray, append
import numpy as np

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
def newej(n):
    print("\n\n")
    print(f"Ej {n} --------------------------------------------------------]")
    print("\n")


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


def ilagrange(xs, ys, z):
    '''
    Recibe una lista de nodos, sus imagenes y una lista de valores a evaluar por el polinomio
    z tiene que ser un ndarray
    '''
    return plagrange(xs, ys)(z)


# 2

def pnewton(xs, ys):
    cnodos = len(xs)

    def ddivididas(i, j):
        assert(i <= j)
        if(i == j):
            return ys[i]
        return (ddivididas(i+1, j)-ddivididas(i, j-1))/(xs[j]-xs[i])

    def prod_raro(i, x):
        r = 1
        for j in range(0, i):
            r *= (x-xs[j])
        return r

    def p(x):
        sum = 0
        for i in range(0, cnodos):
            c = ddivididas(0, i)
            sum += c*prod_raro(i, x)
        return sum

    return p

def pnewtonprim(xs, ys):
    cnodos = len(xs)

    def ddivididas(i, j):
        assert(i <= j)
        if(i == j):
            return ys[i]
        return (ddivididas(i+1, j)-ddivididas(i, j-1))/(xs[j]-xs[i])

    def prod_raro(i, x):
        r = 1
        for j in range(0, i):
            r *= (x-xs[j])
        return r

    def prod_raro_prim(i, x):
        r = 1
        if(i == 0):
            r = 0
        else:
            r = prod_raro_prim(i-1, x)*(x-xs[i-1]) + prod_raro(i-1, x)
        return r
        

    def p(x):
        sum = 0
        for i in range(0, cnodos):
            c = ddivididas(0, i)
            sum += c*prod_raro_prim(i, x)
        return sum

    return p


def inewton(xs, ys, z):
    '''
    Recibe una lista de nodos, sus imagenes y una lista de valores a evaluar por el polinomio.
    z tiene que ser un ndarray
    '''
    return pnewton(xs, ys)(z)

def cubic_inter(xs, ys):
    '''
    Funcion interpolante que usa splines cubicos
    '''
    return interp1d(xs, ys, kind="cubic", bounds_error=False, assume_sorted=True, fill_value="extrapolate")

def ej3():
    newej(3)
    j = arange(1, 102)
    z = 24/25 + j/25

    xs = arange(1,6)
    ys = 1/xs

    print(inewton(xs, ys, z))
    print(ilagrange(xs, ys, z))

def ej4():
    newej(4)

    def ffea(x): return 1/(1+25*(x**2))

    def lab3ej4(n):
        # a

        xj = arange(1,n+2)
        xi = 2*(xj-1)/n - 1
        yi = ffea(xi)


        xs = linspace(-1, 1, 200)


        print("Puntos de interpolacion para el de lagrange: ", xi)
        py = ilagrange(xi, yi, xs)

        # b
        xj = arange(0, n+1)
        xi = np.cos((2*xj+1)*pi/(2*n+2))
        yi = ffea(xi)

        print("Puntos de interpolacion para el de newton: ", xi)
        qy = inewton(xi, yi, xs)

        _, ax = plt.subplots()

        ax.plot(xs, ffea(xs), label="f")
        ax.plot(xs, py, label=f"Lagrange n={n}")
        ax.plot(xs, qy, label=f"Newton n={n}")
        ax.legend()


    # Graficar los 15 graficos

    # for n in range(1, 16):
        # lab3ej4(n)
    lab3ej4(1)
    lab3ej4(5)
    lab3ej4(15)
    plt.show()


def ej5():
    newej(5)
    data = loadtxt("../datos/datos_aeroCBA.dat")

    # Años
    # Sintaxis: data[0:-1, 0] -> Todas las filas, primera columna, 0:-1 se puede escribir como :
    xs_all = data[:, 0]

    # Temps medias
    ys_all = data[:, 2]

    # Sintáxis: not isnan(ys_all) -> array de booleanos(es como usar map, pero numpy lo hace `directamente`)
    # xs_all[arraydebool] -> aplica una máscara (ej: arr[[True, False, False]] devolvería solo el primer elemento si arr tiene 3)
    # Nota: esto funciona así con los array de numpy, que no son los arrays de python
    nanmask = isnan(ys_all)
    # Años con temp media
    xs = xs_all[~nanmask]
    # Años sin temp media
    xsnan = xs_all[nanmask]

    # Temps no nan
    ys = ys_all[~nanmask]


    # Conseguimos una funcion de interpolacion que usar splines cubicos y extrapola a los valores por a fuera del rango
    inter = cubic_inter(xs, ys)

    fig, ax = plt.subplots()
    x = linspace(1956, 2016, 200)

    ax.plot(xs, ys, "o", label="Datos existentes")
    ax.plot(xsnan, inter(xsnan), "o", label="Datos interpolados")
    ax.plot(x, inter(x), label="Funcion interpolante")
    plt.show()

def ej6():
    fig, ax = plt.subplots()
    newej(6)

    xs = asarray([-3., -2., -1., -0., 1 ,2, 3])
    ys = asarray([1, 2, 5, 10, 5, 2, 1])
    x = linspace(-3, 3)

    inter = cubic_inter(xs, ys)
    p = plagrange(xs, ys)
    q = pnewton(xs, ys)

    ax.plot(xs, ys, "o", label="Datos existentes")
    ax.plot(x, inter(x), label="Spline cubico")
    ax.plot(x, p(x), label="Pol Lagrange")
    ax.plot(x, q(x), label="Pol Newton")
    ax.legend()
    plt.show()

def rinterp(fun ,x0, x1, x2, err, mit):
    xs = asarray([x0, x1, x2])
    k = 0
    while fabs(fun(xs[-1])) > err and k<mit:
        q2 = pnewton(xs[-3:], fun(xs[-3:]))
        q2prim = pnewtonprim(xs[-3:], fun(xs[-3:]))
        def f(x): return (q2(x), q2prim(x))

        hx, _ = rnewton(f, xs[-1]+1, err, mit)
        xs = append(xs, hx[-1])
        k += 1
    return xs[-1]


def ej7():
    newej(7)
    def fun(x): return x**6 + 8*x**2 - 15*x
    print(rinterp(fun, -1, 0.5, 3, 1e-7, 500))
