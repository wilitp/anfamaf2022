from math import isinf, sqrt
# 3 Maxima y minima potencia de dos

exp = 0
acc = 1.0

while True:
    if(isinf(acc)):
        break
    acc *= 2
    exp += 1

print("Maxima potencia:", exp) # 1024

exp = 0
acc = 1.0

while True:
    if(acc/2 == 0):
        break
    acc /= 2
    exp -= 1

print("Minima potencia:", exp) # -1074

# 8 Resuelve raices de segundo grado
def mala(a,b,c):
    # usa bashkara
    discr = sqrt(b**2-4*a*c)
    x1 = (-b+discr)/(2*a)
    x2 = (-b-discr)/(2*a)

    return [x1, x2]

[x1, x2] = mala(1,5,6)


print(x1," ", x2)

def buena(a, b, c):
    discr = sqrt(b**2-4*a*c)
    x1 = (-b+discr)/(2*a)
    x2 = c / (a*x1) 

    return (x1, x2)

x1, x2 = buena(1,5,6)
print(x1, x2)


# Aplica el metodo de Horner para evaluar el polinomio

def horn(coefs, x):
    # out = [None]*(len(coefs))

    # Inicializamos en el coef mas grande        
    out = coefs[0]
    for i in range(1, len(coefs)):
        # Multiplicamos la cuenta actual con x si el coeficiente actual no es el de grado 0
        # Sino, solo hacemos la suma a0+...
        if i == len(coefs)-1:
            out = coefs[i]+out
        else:
            out = out*x+coefs[i]
    return out


print(horn([10,8,-6,2,-5,4,2],1)) # 15

def son_reciprocos(x,y):
    return x*y == 1
    
import random
for _ in range(100):
    x = 1 + random.random()
    y = 1/x
    if not son_reciprocos(x,y):
        print(x)
# Esto imprime varios numeros aunque los hayamos definido como inversos explicitmente
# Esto pasa porque la division no siempre es perfecta

# 11

def f(x):
    return sqrt(x**2 + 1) - 1
def g(x):
    return x**2 / (sqrt(x**2 + 1) + 1)

for i in range(20):
    x = 8**-i
    print(f"f(x)={f(x)}, g(x)={g(x)}")

# 12
def son_ortogonales(v,w):
    tmp = (v[0] * v[1]) + (w[0] * w[1])
    print(tmp)
    return tmp == 0
    
x = [1, 1.1024074512658109]
y = [-1, 1/x[1]]
print(son_reciprocos(x[1], y[1]))
if not son_ortogonales(x,y):
    print("Algo salio mal...")

# El problema es x[1] * y[1] no es 1, 
# ya que no tenemos la precision necesaria en la division como para 
# obtener el reciproco exacto de x[1]
