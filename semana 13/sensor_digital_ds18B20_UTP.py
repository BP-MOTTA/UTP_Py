from machine import Pin
from time import sleep
import onewire, ds18x20

#configuracion basica
PIN_1W = 4             # GPIO del bus 1-Wire (DQ)
LED_PIN = 2            # LED de alerta (opcional)
UMBRAL_C = 30.0        # en °C

# --- Inicialización ---
ds_pin = Pin(4)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

led = Pin(LED_PIN, Pin.OUT)
roms = ds_sensor.scan()

if not roms:
    print("No se encontró DS18B20 en GPIO", PIN_1W)
    while True:
        pass

print("DS18B20 encontrado(s):", roms)

while True:
    ds.convert_temp()      # inicia conversión (~750 ms para 12 bits)
    sleep(0.8)             # espera conversión
    # Si hay varios, toma el primero (roms[0]); puedes iterar si deseas varios
    t = ds.read_temp(roms[0])  # en °C (float)
    if t is None:
        print("Lectura inválida")
        continue

    # LED de alerta por umbral
    led.value(1 if t >= UMBRAL_C else 0)

    # Salida simple a consola (puedes copiarla a CSV si quieres)
    estado = "ALERTA" if t >= UMBRAL_C else "OK"
    print(f"temp_c={t:.2f}, estado={estado}")
    sleep(1)
