class Cajero:
    def __init__(self, obj_cuenta):
        self.cuenta = obj_cuenta

    def get_cuenta(self):
        return self.cuenta

    def set_cuenta(self, nueva_cuenta):
        self.cuenta = nueva_cuenta

    def ver_menu(self):
        menu = "\n----------- MENÚ -----------\n"
        menu += "1) Consultar saldo\n"
        menu += "2) Retirar\n"
        menu += "3) Depositar\n"
        menu += "4) Salir"
        return menu

    def consultar_saldo(self):
        return f"Tu saldo actual es: ${self.cuenta.get_saldo():,.2f}"

    def retirar(self, monto):
        return self.cuenta.retirar(monto)

    def depositar(self, monto):
        return self.cuenta.depositar(monto)

    def reporte_final(self):
        movimientos = self.cuenta.get_movimientos()
        reporte = "\n" + "=" * 40 + "\n"
        reporte += "       GRACIAS POR USAR EL CAJERO\n"
        reporte += "=" * 40 + "\n"
        reporte += f"Operaciones realizadas: {len(movimientos)}\n"
        for movimiento in movimientos:
            reporte += f"  {movimiento}\n"
        reporte += f"Saldo final: ${self.cuenta.get_saldo():,.2f}\n"
        reporte += "=" * 40
        return reporte
