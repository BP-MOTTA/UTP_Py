edad=input("Ingrese su edad")
try:
    meses=int(edad)*12
    print(f"los meses que has vivido son: {meses}")
except ValueError:
    print(f"ERROR! ingrese los valores de edad como numero entero, por ejemplo 25")