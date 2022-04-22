
def newej(n):
    print("\n\n")
    print(f"Ej {n} --------------------------------------------------------]")
    print("\n")

# 1


newej(1)


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
    '''
    return list(map(plagrange(xs, ys), z))


# 2
newej(2)


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


def inewton(xs, ys, z):
    '''
    Recibe una lista de nodos, sus imagenes y una lista de valores a evaluar por el polinomio
    '''
    return list(map(pnewton(xs, ys), z))


# Pruebo mis polinomios generadores de polinomios
# en la funcion 1/x
xs = [2, 5/2, 4]
ys = list(map(lambda x: 1/x, xs))
q = pnewton(xs, ys)
p = plagrange(xs, ys)
print(q(11/4))  # 0.35..., que esta bastante cerca
print(p(11/4))  # 0.35..., que esta bastante cerca

newej(3)

z = [24/25 + j/25 for j in range(1, 102)]
xs = list(range(1, 6))
ys = list(map(lambda x: 1/x, xs))
print(inewton(xs, ys, z))
print(ilagrange(xs, ys, z))

