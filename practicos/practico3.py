
def plagrange(xs, ys):
    '''
    A partir de una lista de nodos y otra de sus imagenes, 
    usa el polinomio interpolante de Lagrange para construir un polinomio
    '''
    cnodos = len(xs)
    n = cnodos-1
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
            sum += ys[i]*l(i,x)
        return sum

    return q


# 1 
def ilagrange(xs, ys, z):
    '''
    Recibe una lista de nodos, sus imagenes y una lista de valores a evaluar por el polinomio
    '''
    return list(map(plagrange(xs, ys), z))

# 2

def pnewton(xs, ys):
    cnodos = len(xs)
    def ddivididas(i, j):
        assert(i<=j)
        if(i==j):
            return ys[i]
        return (ddivididas(i+1, j)-ddivididas(i, j-1))/(xs[j]-xs[i])

    def prod_raro(i, x):
        r = 1
        for j in range(0, i):
            r *= (x-xs[i])
        return r
    
    def p(x):
        sum = 0
        for i in range(0, cnodos):
            sum += ddivididas(0, i)*prod_raro(i, x)
        return sum

    return p

# Pruebo evaluando en los valores que debe interpolar
xs = [2, 8]
ys = list(map(lambda x : x**2, xs))
q = pnewton(xs, ys)
print(q(2))