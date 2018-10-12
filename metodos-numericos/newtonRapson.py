#!/usr/bin/python3
"""
@autor elTigueeereMx
    Metodo de NEWTON RAPSON
"""

import math

def poli(x):
    #y=(-0.5*(pow(x,2)))+(2.5*x)+(4.5)
    #y=(5*(pow(x,3)))-(5*(pow(x,2)))+(6*x)-2
    y=(7*(pow(x,5)))-(8*(pow(x,4)))+(44*(pow(x,3)))-(90*(pow(x,2)))+(82*x)-25
    #y=pow(2.7182,x)+pow(2,-x)+ (2*(math.cos(x)))
    return (y)
def deri(x):
    #d=(-1*x)+2.5
    #d=(15*(pow(x,2)))-(10*x)+6
    d=(35*(pow(x,4)))-(36*(pow(x,3)))+(132*(pow(x,2)))-(180*x)-82
    #d=pow(2.7182,x)-((math.log(2))*(pow(2,-x)))-(2*(math.sin(x)))
    return (d)
print ("Método de Newton-Raphson")
x=float(input('Introduce el valor de inicio '))
erroru=float(input('Introduce el error '))
raiz=[ ]
raiz.insert(0,0)
i=0
error=1
print('{:^10}{:^10}{:^10}{:^10}{:^10}'.format('i','VaolorInic','f(xi)','deri,f(xi)','error'))
while abs(error) > erroru:
    fXi=poli(x)
    dFxi=deri(x)
    x1=x-(poli(x)/deri(x))
    raiz.append(x1)
    i=i+1
    x=x1
    error=(raiz[i]-raiz[i-1])/raiz[i]
    print('{:^10}{:^10.4f}{:^10.4f}{:^10.4f}{:^10.4f}'.format(i,float(x),float(fXi),float(dFxi),float(x1)))
print (x)
