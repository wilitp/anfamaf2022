from math import fabs


def rsteffensen(fun, x0, err, mit):
    hx = []
    hf = []
    x_1 = x0

    for k in range(0, mit):
        y_1 = fun(x_1)
        xk = x_1 - y_1**2/(fun(x_1+y_1)-y_1)
        hx += [xk]
        hf += [fun(xk)]
        if fabs(fun(xk)) < err or k > mit:
            break
        x_1 = xk

    return (hx, hf)

def diff_sign(x, y):
    return x > 0 and y < 0 or x < 0 and y > 0

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