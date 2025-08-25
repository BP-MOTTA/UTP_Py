Cod22561=["Juan",35,"Ing. Ambiental",975666666] #listas si cambian
print(f"la edad de {Cod22561[0]} es: {Cod22561[1]} y su numero es el {Cod22561[3]}")

CodJefe=("Pedro",65,"Administrador",939333874) #tupla no cambia
print(f"la edad de {CodJefe[0]} es: {CodJefe[1]} y su numero es el {CodJefe[3]}")

CodNuevo={"nombre":"Ricardo","Edad":19,"Carrera":"Programador","Telefono":998776554}
print(CodNuevo["nombre"])
print(CodNuevo["Edad"])
CodNuevo["nombre"]="Juaneco"
print(CodNuevo["nombre"])
Cod001={"nombre":"Ricardo","Edad":19,"Carrera":"Programador","Telefono":998776554}
Cod002={"nombre":"Marcelo","Edad":19,"Carrera":"Programador","Telefono":998776554}
Central={"Ricardo":Cod001,"Marcelo":Cod002}
Empresa=(Central["Marcelo"])
print(Empresa)