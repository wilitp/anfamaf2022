
def factorial(x):
    if(x <= 0):
        return 1
    else:
        return x * factorial(x-1)


def taylor_seno(n):
    def q(x):
        s = 0
        for k in range(0, n+1):
            aux = 2*k+1
            s += ((-1)**k*(x**aux))/factorial(aux)
        return s
    return q


serie_seno = taylor_seno(4)
