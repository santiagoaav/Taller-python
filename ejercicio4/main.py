from cuenta import Cuenta
from cajero import Cajero


def leer_decimal(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("  Entrada inválida. Ingresa un número.")


print("=== SIMULADOR DE CAJERO AUTOMÁTICO ===\n")

saldo_inicial = leer_decimal("Ingresa el saldo inicial: $")
while saldo_inicial < 0:
    print("  El saldo inicial no puede ser negativo.")
    saldo_inicial = leer_decimal("Ingresa el saldo inicial: $")

obj_cuenta = Cuenta(saldo_inicial)
obj_cajero = Cajero(obj_cuenta)

opcion = ""
while opcion != "4":
    print(obj_cajero.ver_menu())
    opcion = input("Selecciona una opción: ").strip()

    if opcion == "1":
        print(obj_cajero.consultar_saldo())
    elif opcion == "2":
        monto = leer_decimal("Monto a retirar: $")
        print(obj_cajero.retirar(monto))
    elif opcion == "3":
        monto = leer_decimal("Monto a depositar: $")
        print(obj_cajero.depositar(monto))
    elif opcion == "4":
        print(obj_cajero.reporte_final())
    else:
        print("Opción inválida. Elige un número del 1 al 4.")
