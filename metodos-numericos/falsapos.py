#!/usr/bin/python3
"""
@autor elTigueeereMx
    Metodo de FALSAPOSSICION
"""

import math

#Mete polinomio
def polinomio(x):
    #y=(-0.5*(pow(x,2)))+(2.5*x)+(4.5)
    #y=(5*(pow(x,3)))-(5*(pow(x,2)))+(6*x)-2
    y=(7*(pow(x,5)))-(8*(pow(x,4)))+(44*(pow(x,3)))-(90*(pow(x,2)))+(82*x)-25
    return (y)
print("Metodo de puntio fijo")
a=float(input("Ingresa A  "))
b=float(input("Ingresa B  "))
error=float(input("Ingresa error  "))
#var
bucle=False
i=0
aA=polinomio(a)
bB=polinomio(b)
aStr = str(aA)
bStr = str(bB)
xi=((a*(polinomio(b)))-(b*(polinomio(a))))/((polinomio(b))-(polinomio(a)))
if aStr[0] == '-' and bStr[0]!=aStr[0] or bStr[0]=='-' and aStr[0]!=bStr[0]:
    print("cumplio la primera condicion de signos")
    bucle=True
else: 
    print("No cumplio la primera coindicion de signos ADIOOOOOOOOOOOOS")
print('{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}'.format('i','a','b','f(a)','f(b)','xi','f(xi)'))
while bucle:
    i=i+1
    aA=polinomio(a)
    bB=polinomio(b)
    aStr = str(aA)
    bStr = str(bB)
    xi=((a*(polinomio(b)))-(b*(polinomio(a))))/((polinomio(b))-(polinomio(a)))
    evaluandoXi=polinomio(xi)
    evaluandoXiStr = str(evaluandoXi)
    if aStr[0] == evaluandoXiStr[0]:
        a=xi
    else:
        b=xi
    if abs(evaluandoXi) <=  error:
        bucle=False
    print('{:^10}{:^10.4f}{:^10.4f}{:^10.4f}{:^10.4f}{:^10.4f}{:^10.4f}'.format(i,float(a),float(b),float(aA),float(bB),float(xi),float(evaluandoXi)))
print('La raiz es ', xi)