valor_txt = input("ingrese los valores de Temperatura en C: ")
try:
    t=float(valor_txt)
    if t >= 30: #condicion if "condicion 1":
        print("Alerta! Alta Temperatura")
    elif t < 0: #condicion 2
        print("temperatura bajo 0")
    else:
        print("Temperatura normal")
except ValueError:
    print("Entrada inválida. Use números (ej. 26.5).")