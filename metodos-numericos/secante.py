#!/usr/bin/python3
"""
@autor elTigueeereMx
    Metodo de SECANTE
"""

import math

#fUNCION
def poli(x):
    #y=pow(x,2)-3.0*x-4
    y=(7*(pow(x,5)))-(8*(pow(x,4)))+(44*(pow(x,3)))-(90*(pow(x,2)))+(82*x)-25
    return (y)

print ("Método de la secante")

x1=float(input('Introduce el valor de inicio x1: '))
x0=float(input('Introduce el valor de inicio x0: '))
erroru=float(input('Introduce el error '))
raiz=[]
raiz.insert(0,0)
i=0
error=1
print("Contemplar la primera iteracion")
print('{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}'.format('i','x1','x0','f(x1)','F(xi-1)','x2','error'))
#print('{:^10}{:^10.4f}{:^10.4f}{:^10.4f}{:^10}{:^10.4f}'.format(i,float(x1),float(x0),(poli(x1)),(poli(x0)),'aunNo',error))
while abs(error) > erroru :
    x2 = x1 - (poli(x1)*(x1-x0))/(poli(x1)-poli(x0))
    raiz.append(x2)
    x0 = x1
    x1 = x2
    i=i+1
    error=(raiz[i]-raiz[i-1])/raiz[i]
    print('{:^10}{:^10.4f}{:^10.4f}{:^10.4f}{:^10.4f}{:^10.4f}'.format(i,float(x1),float(x0),(poli(x1)),(poli(x0)),x2,error))
print(x2) 
