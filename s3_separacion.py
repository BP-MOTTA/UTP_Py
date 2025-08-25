import random as rd
Vingreso=[] #lista vacia
for i in range (15): #incio de un bucle es con el : el identado es importante
    Vingreso.append(rd.randint(1,30)) #append añade a la lista
print(Vingreso) 

Vmayor=[]
Vmenor=[]
for i in Vingreso:
    if i >= 5:
        Vmayor.append(i)
    else:
        Vmenor.append(i)
print(Vmayor)
print(Vmenor)

#hacer que el codigo genere 20 valores hasta 30V en aleatorio
#separarlos en valores, bajo, medios y altos 
# y mostrarlos en salida
