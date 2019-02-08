#!/usr/bin/python3
import os
from scipy.interpolate import lagrange
import matplotlib.pyplot as elpyplot

#PUNTOS EN x & Y
x = []
y = []

def lagranch(evaluadoX):
    #ECHANLO EL POLINOMIO DE LA GRANGE
    p=lagrange(x,y)
    print("El polinomio es:: \n")
    print(p)
    print("Evaluado en X=" + str(evaluadoX) )
    print(p(evaluadoX))

    #ECHANDO LA GRAF
    elpyplot.plot(x,y,"o")
    elpyplot.xlabel("X")
    elpyplot.ylabel("Y")
    elpyplot.show()
    return 0

def lalo():
    os.system('clear')
    n=1
    enX=raw_input("Ingresa X1 ")
    while enX != "":
        n+=1
        x.append(float(enX))
        enX = raw_input("Ingresa X" + str(n) + " O enter para pasar con Y "  )
    os.system('clear')
    i=1
    enY=raw_input("Ingresa Y! ")
    while enY != "":
        i+=1
        y.append(float(enY))
        enY = raw_input("Ingresa Y" + str(i) + " O solo enter para salir ")
    os.system('clear')    
    evalurX=int(raw_input("Evaluar en x en el punto "))
    os.system('clear')
    print("En X es " + str(x))
    print("En Y es " + str(y))
    lagranch(evalurX)

lalo()