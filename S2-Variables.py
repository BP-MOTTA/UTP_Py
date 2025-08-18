NOMBRE = "Bryan"       # constante por convención - str
edad = 20              # int
voltaje = 3.14159      # float
activo = True          # bool
#f-string (formato para cadenas de caracteres, letras)
print(f"Hola, {NOMBRE}. Edad: {edad}")
# para float {voltaje:.5f} el valor antes del f nos dice el numero despues de la coma decimal
print(f"Voltaje: {voltaje:.5f} V | Activo: {activo}")
print(f"Tipos -> edad:{type(edad).__name__}, voltaje:{type(voltaje).__name__}")
