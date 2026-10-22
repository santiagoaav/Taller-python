class Inventario:
    def __init__(self, nombre_tienda):
        self.nombre_tienda = nombre_tienda
        self.productos = []

    def get_nombre_tienda(self):
        return self.nombre_tienda

    def set_nombre_tienda(self, nuevo_nombre):
        self.nombre_tienda = nuevo_nombre

    def get_productos(self):
        return self.productos

    def agregar_producto(self, obj_producto):
        obj_producto.clasificar_stock()
        self.productos.append(obj_producto)

    def existe_codigo(self, codigo):
        for obj_producto in self.productos:
            if obj_producto.get_codigo() == codigo:
                return True
        return False

    def ver_estado(self, obj_producto):
        categoria = obj_producto.get_categoria()
        if categoria == "crítico":
            mensaje = "CRÍTICO - reabastecimiento urgente"
        elif categoria == "bajo stock":
            mensaje = "BAJO STOCK"
        else:
            mensaje = "SUFICIENTE"
        return f"{obj_producto.ver_info()} -> {mensaje}"

    def total_unidades(self):
        total = 0
        for obj_producto in self.productos:
            total += obj_producto.get_cantidad()
        return total

    def generar_reporte(self):
        categorias = ["crítico", "bajo stock", "suficiente"]

        reporte = "\n" + "=" * 55 + "\n"
        reporte += f"   REPORTE CONSOLIDADO - {self.nombre_tienda.upper()}\n"
        reporte += "=" * 55 + "\n"

        for categoria in categorias:
            cantidad_productos = 0
            unidades = 0
            detalle = ""
            for obj_producto in self.productos:
                if obj_producto.get_categoria() == categoria:
                    cantidad_productos += 1
                    unidades += obj_producto.get_cantidad()
                    detalle += f"   - {obj_producto.ver_info()}\n"
            reporte += f"\n{categoria.upper()}: {cantidad_productos} producto(s), {unidades} unidades\n"
            reporte += detalle

        reporte += "\n" + "-" * 55 + "\n"
        reporte += f"Total de productos: {len(self.productos)}\n"
        reporte += f"Total de unidades: {self.total_unidades()}\n"
        reporte += "=" * 55
        return reporte
