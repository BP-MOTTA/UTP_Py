#Busca la ruta donde esta el codigo y luego se añade la ruta del archivo de ingreso
from pathlib import Path #importo el comando path (busca el lugar del codigo)
ROOT = Path(__file__).resolve().parents[0]  # sube desde src/ a la raíz del proyecto C:\Users\BP_motta\python_UTP\UTP_Py
TXT  = ROOT / "archivos"/ "mediciones_basico.txt"

valores=[]
with open(TXT,'r',encoding='"utf-8"') as f:
    for linea in f: #lee linea por linea del archivo ingresado
        s=linea.strip()
        if not s or s.startswith("#"):
            continue
        if not s or s.startswith("!"):
            continue
        s = s.replace(",", ".")           # acepta coma decimal
        try:
            valores.append(float(s))
        except ValueError:
            #si no es ni linea ni numero, debe saltarlo
            pass
        
Vmayor=[]
Vmenor=[]
for i in valores:
    if i >= 5:
        Vmayor.append(i)
    else:
        Vmenor.append(i)
print(Vmayor)
print(Vmenor)

print(len(Vmayor))
print(len(Vmenor))

