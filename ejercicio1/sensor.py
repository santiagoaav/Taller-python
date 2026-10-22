class Sensor:
    def __init__(self, numero, temperatura):
        self.numero = numero
        self.temperatura = temperatura
        self.categoria = ""
        self.accion = ""

    def get_numero(self):
        return self.numero

    def get_temperatura(self):
        return self.temperatura

    def set_temperatura(self, nueva_temperatura):
        self.temperatura = nueva_temperatura

    def get_categoria(self):
        return self.categoria

    def get_accion(self):
        return self.accion

    def clasificar(self):
        if self.temperatura < 18:
            self.categoria = "fría"
            self.accion = "Se enciende la calefacción"
        elif self.temperatura <= 25:
            self.categoria = "óptima"
            self.accion = "Sin acción"
        else:
            self.categoria = "caliente"
            self.accion = "Se activa el aire acondicionado"
        return self.categoria

    def ver_info(self):
        info = (f"Sensor {self.numero}: {self.temperatura:.1f}°C -> "
                f"{self.categoria.upper()} | {self.accion}")
        return info
