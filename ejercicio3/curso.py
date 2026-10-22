class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def get_estudiantes(self):
        return self.estudiantes

    def agregar_estudiante(self, obj_estudiante):
        self.estudiantes.append(obj_estudiante)

    def promedio_curso(self):
        suma = 0
        for obj_estudiante in self.estudiantes:
            suma += obj_estudiante.calcular_promedio()
        return suma / len(self.estudiantes)

    def mejor_estudiante(self):
        mejor = self.estudiantes[0]
        for obj_estudiante in self.estudiantes:
            if obj_estudiante.calcular_promedio() > mejor.calcular_promedio():
                mejor = obj_estudiante
        return mejor

    def peor_estudiante(self):
        peor = self.estudiantes[0]
        for obj_estudiante in self.estudiantes:
            if obj_estudiante.calcular_promedio() < peor.calcular_promedio():
                peor = obj_estudiante
        return peor

    def contar_aprobados(self):
        aprobados = 0
        for obj_estudiante in self.estudiantes:
            if obj_estudiante.aprobo():
                aprobados += 1
        return aprobados

    def contar_por_categoria(self):
        conteo = {"reprobado": 0, "regular": 0, "bueno": 0, "excelente": 0}
        for obj_estudiante in self.estudiantes:
            conteo[obj_estudiante.determinar_categoria()] += 1
        return conteo

    def ver_resumen(self):
        total = len(self.estudiantes)
        aprobados = self.contar_aprobados()
        reprobados = total - aprobados
        mejor = self.mejor_estudiante()
        peor = self.peor_estudiante()
        conteo = self.contar_por_categoria()

        resumen = "\n" + "=" * 60 + "\n"
        resumen += f"   RESUMEN ESTADÍSTICO - {self.nombre.upper()}\n"
        resumen += "=" * 60 + "\n"
        resumen += f"Total de estudiantes : {total}\n"
        resumen += f"Promedio del curso   : {self.promedio_curso():.2f}\n"
        resumen += f"Promedio más alto    : {mejor.calcular_promedio():.2f} ({mejor.get_nombre()})\n"
        resumen += f"Promedio más bajo    : {peor.calcular_promedio():.2f} ({peor.get_nombre()})\n"
        resumen += f"Aprobados            : {aprobados} ({aprobados / total * 100:.1f}%)\n"
        resumen += f"Reprobados           : {reprobados} ({reprobados / total * 100:.1f}%)\n"
        resumen += "\nEstudiantes por categoría:\n"
        for categoria in conteo:
            resumen += f"  {categoria.capitalize():<10}: {conteo[categoria]}\n"
        resumen += "=" * 60
        return resumen
