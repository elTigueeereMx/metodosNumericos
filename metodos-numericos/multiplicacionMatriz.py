"""
Creado en Oct18
@autor: eltigueeereMx
"""
import numpy
import sys 
print("Programa para calcular la multiplicacion de matrices")
r1=int(input("Numero de renglones de la matriz 1::: "))
c1=int(input("Numero de colubnas de la matriz 1::: "))
r2=int(input("Numero de renglones de la matriz 2::: "))
c2=int(input("Numero de colubnas de la matriz 2::: "))
#verificando si se puede hacer la matriz
if(c1 != r2):
    print("No se puede hacer la multiplicacion de matriz")
    sys.exit() #me sace del programa
#inicializando la matriz
matriz1=numpy.zeros((r1,c1))
matriz2=numpy.zeros((r2,c2))
#viendo la dimencion de la matriz resultado
matrizR=numpy.zeros((r1,c2))
#capturando matriz
print("Introduce los elementos de la matriz UNO")
for r in range(0,r1):
    for c in range(0,c1):
        matriz1[r,c]=input("Elemento a[" + str(r+1) + str(c+1) + "]"  )
print("Introduce los elementos de la matriz DOS")
for r in range(0,r2):
    for c in range(0,c2):
        matriz2[r,c]=input("Elemento a[" + str(r+1) + str(c+1) + "]"  )
#operaciuones
for r in range(0,r1):
    for c in range(c2):
        for m in range(0,r2):
            matrizR[r,c]+=matriz1[r,m]*matriz2[m,c]
print(matrizR)