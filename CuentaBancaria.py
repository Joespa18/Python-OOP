# Crea una clase CuentaBancaria con los atributos tasa de interés y balance
class CuentaBancaria:

    cuentas = [] #Bonus
    def __init__(self, tipo, tasa_interes, balance=0):
        self.tipo = tipo
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.cuentas.append(self) #Bonus

    # Agrega un método depósito a la clase CuentaBancaria
    def deposito(self, monto_deposito):
        self.balance += monto_deposito
        return self

    # Agrega un método retiro a la clase CuentaBancaria
    def retiro(self, monto_retiro):
        self.balance -= monto_retiro
        return self

    # Agrega un método mostrar_info_cuenta retiro a la clase CuentaBancaria
    def mostrar_info_cuenta(self):
        print(f"tipo cuenta: {self.tipo} - Tasa: {self.tasa_interes} - Balance: {self.balance}")
        return self
    
    # Agrega un método generar_interés a la clase CuentaBancaria
    def generar_interes(self):
        if self.balance > 0:
            self.balance = self.balance*(1 + self.tasa_interes)
        else:
            print("Sin saldo")
        return self

    # BONUS NINJA: utiliza un método de clase para imprimir todas las instancias de la información de una cuenta bancaria
    @classmethod
    def todas_las_cuentas(cls):
        for cuenta in cls.cuentas:
            cuenta.mostrar_info_cuenta()

# Crea 2 cuentas
cuenta1 = CuentaBancaria('cuenta corriente', 0.012)
cuenta2 = CuentaBancaria('cuenta ahorro', 0.016, 2000)

# Para la primera cuenta, haz 3 depósitos y 1 retiro, luego genera intereses y muestra la información de la cuenta, todo en una línea de código (es decir, encadenando)
cuenta1.deposito(500).deposito(1000).deposito(500).retiro(1000).generar_interes().mostrar_info_cuenta()

# Para la segunda cuenta, haz 2 depósitos y 4 retiros, luego genera intereses y muestra la información de la cuenta, todo en una línea de código (es decir, encadenando)
cuenta2.deposito(500).deposito(500).retiro(250).retiro(250).retiro(500).retiro(1000).generar_interes().mostrar_info_cuenta()

# Bonus Ninja
CuentaBancaria.todas_las_cuentas()