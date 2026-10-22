from sensor import Sensor
from edificio import Edificio


def leer_entero(mensaje, minimo):
    while True:
        try:
            valor = int(input(mensaje))
            if valor >= minimo:
                return valor
            print(f"  El valor debe ser mayor o igual a {minimo}.")
        except ValueError:
            print("  Entrada inválida. Ingresa un número entero.")


def leer_decimal(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("  Entrada inválida. Ingresa un número (ej: 21.5).")


print("=== SISTEMA DE CONTROL DE SENSORES DE TEMPERATURA ===\n")

obj_edificio = Edificio("Edificio principal")
cantidad = leer_entero("¿Cuántos sensores hay instalados? ", 1)

for i in range(1, cantidad + 1):
    temperatura = leer_decimal(f"\nTemperatura del sensor {i} (°C): ")
    obj_sensor = Sensor(i, temperatura)
    obj_edificio.agregar_sensor(obj_sensor)
    print("  " + obj_sensor.ver_info())

print(obj_edificio.ver_resumen())
