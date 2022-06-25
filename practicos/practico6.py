from numpy import ndarray
import numpy as np


'''
1. Escribir dos funciones en python llamadas soltrsup y soltrinf que resuelvan el sistema
lineal Ax = b, donde A es una matriz triangular (superior e inferior, respectivamente).
La entrada debe ser (A,b) con A∈ Rnxn matriz triangular y b∈ Rn, y la salida debe ser la solución x. 
Se debe imprimir un mensaje de error si la matriz es singular.
'''

def soltrinf(A: ndarray, b: ndarray) -> ndarray:
    n = len(b)
    sol = np.zeros(n)
    for i in range(0, n):
        sum = 0 # Variable para sumar los coeficientes por las partes de la solucion que ya saque
        for j in range(0, i):
            sum += sol[j] * A[i, j]
        sol[i] = (b[i] - sum)/A[i, i]
    return sol

def soltrsup(A: ndarray, b: ndarray) -> ndarray:
    B = np.flip(A, 0) # Doy vuelta las filas
    return soltrinf(B, b) # Resuelvo como triangular inferior


'''
2. 
a) Escribir una función llamada "egauss" que implemente el método de eliminación Gaussiana. 
Debe tener entrada (A,b) con A∈ Rnxn y b∈ Rn, con salida [U,y] con U ∈ Rnxntriangular superior e y ∈ Rn
.
b) Escribir una función llamada "soleg" que resuelva sistemas lineales Ax = b usando
eliminación Gaussiana y resolviendo el sistema triangular superior Ux = y (usando soltrsup). 
Debe tener entrada (A,b) con A∈ Rnxn y b∈ Rn y, la salida debe ser la solución x
'''

def egauss(A: ndarray, b: ndarray):
    n = len(b)
    y = np.copy(b)
    U = np.copy(A)


    for k in range(0, n): # por cada pivot
        for i in range(k+1, n): # por cada fila abajo del pivot
            if(U[k, k] == 0):
                raise Exception("Un pivote quedó 0, no se puede seguir")
            m = U[i, k] / U[k, k]
            for j in range(0, n): # por cada elemento de la fila a la derecha de la diagonal(inclusive)
                if j < k+1:
                    U[i, j] = 0
                else:
                    U[i, j] = U[i, j] - m*U[k, j]
            y[i] = y[i] - m*y[k]

    return (U, y)

def soleg(A: ndarray, b:ndarray):
    U, y = egauss(A, b)
    return soltrsup(U, y)

