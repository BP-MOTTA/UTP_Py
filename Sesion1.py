import datetime as dt #importar funciones - modulo fecha
import random as rd #importar funciones - modulo aleatorio
nombre = "Bryan" #constantes
fecha = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S") # variable
#definir valores aleatorios
print("hola " + nombre)
print( fecha) # salida de variable
for i in range(10): #bucle for
    v = rd.randint(0, 1023) #valor aleatorio entre 1 y 100
    if v < 100: #condicion
        print("valor bajo: " + str(v)) # salida de variable 
    elif v < 500: #condicion
        print("valor medio: " + str(v)) # salida de variable 

#trabajo 1: Generar un correo electronico con el nombre y la fecha que le diga al ing en jefe
#los valores medidos por el sensor y la fecha de medicion.

#Tarea 1: Generen un correo electronico con el nombre del ingerio, la fecha del informe, 15 valores medidos donde 
