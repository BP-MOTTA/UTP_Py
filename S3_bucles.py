import numpy as np #Paqueteria matematica-Fisica
Suma=0
#metodo numerico
for i in range(1,500): #Repeticiones de 1 hasta 499
    Suma= Suma+(1/(i**2)) #sumatoria de 1/n^2 = Pi^2/6
print(Suma)
#solucion analitica
print(np.pi**2/6)

import random as rd
lista=[] #se crea una lista vacia dando una variable e igualandola a []
for i in range(10): #todos los bucles y las condicionales deben terminar con : 
    lista.append(rd.randint(1,10))#python es muy delicado con los identado (Tab)
print(lista) #el comando.append agrega a la lista


vol_sqrt=[]
V = [4.5, 2.32, 4.88]
for i in V: #generar operaciones en listas dandole valores de una lista al i
    vol_sqrt.append(i**2)
print(f"los valores del voltaje ingresados son {V} y sus cuadrados son {vol_sqrt}")

lecturas = [4.95, 5.10, 4.88]
for i,vol in enumerate(lecturas, start=1):
    print(f"el valor de la medicion {i} es {vol}V")