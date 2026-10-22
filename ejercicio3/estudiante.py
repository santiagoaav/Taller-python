class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def get_notas(self):
        return self.notas

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def calcular_promedio(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def determinar_categoria(self):
        promedio = self.calcular_promedio()
        if promedio < 3.0:
            categoria = "reprobado"
        else:
            if promedio < 4.0:
                categoria = "regular"
            else:
                if promedio <= 4.5:
                    categoria = "bueno"
                else:
                    categoria = "excelente"
        return categoria

    def aprobo(self):
        return self.determinar_categoria() != "reprobado"

    def ver_info(self):
        notas_texto = ", ".join(f"{nota:.1f}" for nota in self.notas)
        info = (f"{self.nombre:<12} Notas: [{notas_texto}]  "
                f"Promedio: {self.calcular_promedio():.2f} -> "
                f"{self.determinar_categoria().upper()}")
        return info
