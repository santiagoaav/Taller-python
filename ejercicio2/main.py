from producto import Producto
from inventario import Inventario


def leer_entero(mensaje, minimo):
    while True:
        try:
            valor = int(input(mensaje))
            if valor >= minimo:
                return valor
            print(f"  El valor debe ser mayor o igual a {minimo}.")
        except ValueError:
            print("  Entrada inválida. Ingresa un número entero.")


def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("  Este campo no puede quedar vacío.")


print("=== GESTOR DE INVENTARIO DE SUPERMERCADO ===\n")

obj_inventario = Inventario("Supermercado")
cantidad = leer_entero("¿Cuántos productos hay en el inventario? ", 1)

for i in range(1, cantidad + 1):
    print(f"\n--- Producto {i} de {cantidad} ---")

    codigo = leer_texto("Código: ").upper()
    while obj_inventario.existe_codigo(codigo):
        print("  Ese código ya existe.")
        codigo = leer_texto("Código: ").upper()

    nombre = leer_texto("Nombre: ")
    unidades = leer_entero("Cantidad disponible: ", 0)

    obj_producto = Producto(codigo, nombre, unidades)
    obj_inventario.agregar_producto(obj_producto)

print("\n=== ESTADO DE CADA PRODUCTO ===")
for obj_producto in obj_inventario.get_productos():
    print(obj_inventario.ver_estado(obj_producto))

print(obj_inventario.generar_reporte())
