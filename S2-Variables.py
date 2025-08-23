NOMBRE = "Bryan"       # constante por convención - str (textos)
edad = 35              # int (enteros)
voltaje = 3.1415945798 # float (decimales - puntos flotantes)
activo = False          # bool (Logico)
#f-string (formato para cadenas de caracteres, letras - Formato)
print(f"Hola, {NOMBRE}, Edad: {edad}")
# para float {voltaje:.5f} el valor antes del f nos dice el numero despues de la coma decimal
print(f"Voltaje: {voltaje:.4f} V | Activo: {activo}")
print(f"Tipos -> edad:{type(edad).__name__}, voltaje:{type(voltaje).__name__}")

print(f"cambio de tipo de variable, inicialmente {edad} es del tipo {type(edad).__name__}")
print(f"ahora usando el comando str, el valor {str(edad)}, es del tipo {type(str(edad)).__name__}")