from estudiante import Estudiante
from curso import Curso


def leer_entero(mensaje, minimo):
    while True:
        try:
            valor = int(input(mensaje))
            if valor >= minimo:
                return valor
            print(f"  El valor debe ser mayor o igual a {minimo}.")
        except ValueError:
            print("  Entrada inválida. Ingresa un número entero.")


def leer_nota(mensaje):
    while True:
        try:
            nota = float(input(mensaje))
            if 0.0 <= nota <= 5.0:
                return nota
            print("  La nota debe estar entre 0.0 y 5.0.")
        except ValueError:
            print("  Entrada inválida. Ingresa un número (ej: 3.8).")


print("=== CALCULADORA DE CALIFICACIONES ACADÉMICAS ===\n")

obj_curso = Curso("Curso de programación")
cantidad = leer_entero("¿Cuántos estudiantes tiene el curso? ", 1)

for i in range(1, cantidad + 1):
    print(f"\n--- Estudiante {i} de {cantidad} ---")
    nombre = input("Nombre: ").strip()
    if nombre == "":
        nombre = f"Estudiante {i}"

    obj_estudiante = Estudiante(nombre)
    for n in range(1, 5):
        nota = leer_nota(f"  Calificación {n}: ")
        obj_estudiante.agregar_nota(nota)

    obj_curso.agregar_estudiante(obj_estudiante)

print("\n=== RESULTADOS INDIVIDUALES ===")
for obj_estudiante in obj_curso.get_estudiantes():
    print(obj_estudiante.ver_info())

print(obj_curso.ver_resumen())
