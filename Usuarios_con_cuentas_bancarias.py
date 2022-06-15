class CuentaBancaria:

    def __init__(self, tasa_interes, balance=0):
        self.tasa_interes = tasa_interes
        self.balance = balance

    def deposito(self, monto_deposito):
        self.balance += monto_deposito
        return self

    def retiro(self, monto_retiro):
        self.balance -= monto_retiro
        return self

    def mostrar_info_cuenta(self):
        print(f"Tasa: {self.tasa_interes} - Balance: {self.balance}")
        return self

    def generar_interes(self):
        if self.balance > 0:
            self.balance = self.balance*(1 + self.tasa_interes)
        else:
            print("Sin saldo")
        return self

# Actualizar el método __init__ de la clase Usuario
class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.cuenta = CuentaBancaria(tasa_interes=0.02, balance=0)

    def agregar_cuenta(self, nombre_cuenta):
        self.cuenta += nombre_cuenta

    # Actualizar el método hacer_depósito de la clase Usuario
    def hacer_depósito(self, monto_deposito):
        self.cuenta.balance += monto_deposito
        return self
    # Actualizar el método hacer_retiro de la clase Usuario
    def hacer_retiro(self, monto_retiro):
        self.cuenta.balance -= monto_retiro
        return self
    # Actualizar el método mostrar_balance_usuario de la clase Usuario
    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.nombre} - Saldo: {self.cuenta.balance}")
        return self

    def transferencia (self, monto, usuario):
        self.cuenta.balance -= monto
        usuario.cuenta.balance += monto
        print("\nSaldo después de la transferencia:")
        self.mostrar_balance_usuario()
        usuario.mostrar_balance_usuario()
        return self

jose = Usuario("José Sepúlveda","jose@dojo.cl")
esteban = Usuario("Esteban Pareja","esteban@dojo.cl")
juan = Usuario("Juan Perez", "juan@dojo.cl")

jose.hacer_depósito(100).hacer_depósito(100).hacer_depósito(100).hacer_retiro(50).mostrar_balance_usuario()

esteban.hacer_depósito(100).hacer_depósito(200).hacer_retiro(50).hacer_retiro(100).mostrar_balance_usuario()

juan.hacer_depósito(500).hacer_retiro(100).hacer_retiro(100).hacer_retiro(100).mostrar_balance_usuario()

jose.transferencia(150, juan)
