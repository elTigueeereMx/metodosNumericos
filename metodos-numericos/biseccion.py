#!/usr/bin/python3
"""
@autor elTigueeereMx
    Metodo de BISSECION
"""

import math

#Función para polinomios
def poli(x):
    #y=(-0.5*(pow(x,2)))+(2.5*x)+(4.5)
    #y=(5*(pow(x,3)))-(5*(pow(x,2)))+(6*x)-2
    y=(7*(pow(x,5)))-(8*(pow(x,4)))+(44*(pow(x,3)))-(90*(pow(x,2)))+(82*x)-25
    return (y)
#Programa principal
print ("Biseccion metodo de bisección")
xi=float(input('Introduce el valor de xi '))
xs=float(input('Introduce el valor de xs '))
error=float((input('Introduce el error ')))
xa = (xi+xs)/2.0
i=0
print('{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}'.format('i','xi','xs','xa','signo','cambio','error'))
while abs(poli(xa)) > error:
    i=i+1
    xa = (xi+xs)/2.0
    if poli(xi)*poli(xa) < 0:
        xs=xa
        signo="Negativo"
        limite="Superior"
    else:
        xi=xa
        signo="Postivo"
        limite="Inferior"
    print('{:^10}{:^10.4f}{:^10.4f}{:^10.4f}{:^10}{:^10}{:^10.4f}'.format(i,float(xi),float(xs),float(xa),signo,limite,(poli(xa))))
print("La raíz es: ",xa)
