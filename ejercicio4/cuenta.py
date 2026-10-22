class Cuenta:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
        self.movimientos = []

    def get_saldo(self):
        return self.saldo

    def get_movimientos(self):
        return self.movimientos

    def retirar(self, monto):
        if monto <= 0:
            mensaje = "El monto a retirar debe ser mayor que cero."
        elif monto > self.saldo:
            mensaje = (f"Saldo insuficiente. Intentaste retirar ${monto:,.2f} "
                       f"y tu saldo es ${self.saldo:,.2f}.")
        else:
            self.saldo -= monto
            self.movimientos.append(f"Retiro    ${monto:,.2f}")
            mensaje = f"Retiro exitoso de ${monto:,.2f}. Nuevo saldo: ${self.saldo:,.2f}"
        return mensaje

    def depositar(self, monto):
        if monto <= 0:
            mensaje = "Monto inválido. El depósito debe ser un valor positivo."
        else:
            self.saldo += monto
            self.movimientos.append(f"Depósito  ${monto:,.2f}")
            mensaje = f"Depósito exitoso de ${monto:,.2f}. Nuevo saldo: ${self.saldo:,.2f}"
        return mensaje
