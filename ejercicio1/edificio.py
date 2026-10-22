class Edificio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.sensores = []
        self.conteo = {"fría": 0, "óptima": 0, "caliente": 0}

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def get_sensores(self):
        return self.sensores

    def get_conteo(self):
        return self.conteo

    def agregar_sensor(self, obj_sensor):
        categoria = obj_sensor.clasificar()
        self.sensores.append(obj_sensor)
        self.conteo[categoria] += 1

    def calcular_promedio(self):
        if len(self.sensores) == 0:
            return 0
        suma = 0
        for obj_sensor in self.sensores:
            suma += obj_sensor.get_temperatura()
        return suma / len(self.sensores)

    def ver_resumen(self):
        resumen = "\n" + "=" * 50 + "\n"
        resumen += f"   RESUMEN DE TEMPERATURAS - {self.nombre.upper()}\n"
        resumen += "=" * 50 + "\n"
        resumen += f"Total de habitaciones: {len(self.sensores)}\n"
        resumen += f"  Frías     (< 18°C)      : {self.conteo['fría']}  -> calefacción encendida\n"
        resumen += f"  Óptimas   (18°C - 25°C) : {self.conteo['óptima']}  -> sin acción\n"
        resumen += f"  Calientes (> 25°C)      : {self.conteo['caliente']}  -> aire acondicionado activado\n"
        resumen += f"\nTemperatura promedio: {self.calcular_promedio():.1f}°C\n"
        resumen += "=" * 50
        return resumen
