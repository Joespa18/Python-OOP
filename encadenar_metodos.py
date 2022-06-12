# Crea un archivo con la clase Usuario, incluyendo los métodos __init__ y hacer_depósito
class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.saldo = 0
    def hacer_depósito(self, monto):
        self.saldo += monto
        return self
    # Agrega un método hacer_retiro a la clase Usuario
    def hacer_retiro(self, monto):
        self.saldo -= monto
        return self
    # Agrega un método mostrar_balance_usuario a la clase Usuario
    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.nombre} - Saldo: {self.saldo}")
        return self
    # BONUS: transfer_dinero(self, other_user, amount): haz que este método reduzca el balance del usuario por el monto y agrega esa cantidad al balance de otro_usuario
    def transferencia (self, monto, usuario):
        self.saldo -= monto
        usuario.saldo += monto
        print("\nSaldo después de la transferencia:")
        self.mostrar_balance_usuario()
        usuario.mostrar_balance_usuario()
        return self

# Crea 3 instancias de la clase Usuario
jose = Usuario("José Sepúlveda","jose@dojo.cl")
esteban = Usuario("Esteban Pareja","esteban@dojo.cl")
juan = Usuario("Juan Perez", "juan@dojo.cl")

# Haz que el primer usuario haga 3 depósitos y 1 giro, y luego muestra sus balances
jose.hacer_depósito(100).hacer_depósito(100).hacer_depósito(100).hacer_retiro(50).mostrar_balance_usuario()

# Haz que el segundo usuario haga 2 depósitos y 2 giros, y luego muestra sus balances
esteban.hacer_depósito(100).hacer_depósito(200).hacer_retiro(50).hacer_retiro(100).mostrar_balance_usuario()

# Haz que el tercer usuario haga 1 depósito y 3 giros, y luego muestra sus balances
juan.hacer_depósito(500).hacer_retiro(100).hacer_retiro(100).hacer_retiro(100).mostrar_balance_usuario()

# BONUS: Agrega un método transferir_dinero; haz que el primer usuario transfiera dinero al tercer usuario y luego imprime los balances de ambos usuarios
jose.transferencia(150, juan)