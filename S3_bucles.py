import random as rd
lista=[] #lista vacia
for i in range (5): #incio de un bucle es con el : el identado es importante
    num=rd.randint(1,10) #genera son numeros aleatorios del 1 al 10
    lista.append(num) #append añade a la lista
print(lista)

vol_sqrt=[]
V = [4.5, 2.32, 4.88]
for i in V:
    vol_sqrt.append(i*i)
print(f"el voltaje al cuadrado es: {vol_sqrt}") #comando map

lecturas = [4.95, 5.10, 4.88]
for idx, vol in enumerate(lecturas, start=1):
    print(f"{idx}: {vol:.2f} V")
    
#primero crear una lista aleatoria de 10 valores menores a 10V
#verificar si los valores son mayores o menores a 5V
#imprimir en cada caso voltaje alto o voltaje bajo

