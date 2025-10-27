from machine import Pin
import time

LED = Pin(2, Pin.OUT)
BNT = Pin(4, Pin.IN, Pin.PULL_UP)

# dos periodos de parpadeo (segundos)
SLOW = 0.01
FAST = 0.3
period = SLOW

print("inicio del proyecto --- pulse el boton")

while True:
    if BNT.value()==0:
        period = FAST if period == SLOW else SLOW
        print("velocidad:", "Rapida" if period == FAST else "Lenta")
        time.sleep(0.25)
        while BNT.value()==0:
            time.sleep(0.01)

    LED.value(1)
    time.sleep(period)
    LED.value(0)
    time.sleep(period)
