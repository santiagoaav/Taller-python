class Producto:
    def __init__(self, codigo, nombre, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.categoria = ""

    def get_codigo(self):
        return self.codigo

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def get_categoria(self):
        return self.categoria

    def clasificar_stock(self):
        if self.cantidad < 10:
            self.categoria = "crítico"
        elif self.cantidad <= 50:
            self.categoria = "bajo stock"
        else:
            self.categoria = "suficiente"
        return self.categoria

    def ver_info(self):
        info = f"[{self.codigo}] {self.nombre} - {self.cantidad} unidades"
        return info
