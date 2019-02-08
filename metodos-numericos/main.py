#!/usr/bin/python3
import os

def menuPrincipal():
    op=""
    print ("\n\n\t1.-Pol. Lagrange")
    print ("\n\tsalir.-salir")
    op=input("\n\n\tElige una opcion ")
    return op

def polinomioLagrange():
	from polinomioLagrange import lalo
	return 0

salir = False
opcion = ""

while not salir:
    opcion = menuPrincipal() 
    if opcion == 1:
        os.system('clear')
        polinomioLagrange()
    elif opcion == salir:
        salir = True
    else:
        os.system('clear')
        print ("\n\t*****************Introduce la opcion correcta*****************")

print ("Fin")
