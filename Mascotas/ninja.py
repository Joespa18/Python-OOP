from info_mascota import Mascota

#Crea una clase Ninja con los atributos ninja mencionados anteriormente.
class Ninja:
    def __init__(self, nombre, apellido, comida_mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.comida_mascota = comida_mascota
        self.mascota = Mascota(nombre='Totó', tipo='perro', golosinas='huesitos', salud= 100, energia= 100)

# Implementa caminar(), alimentar(), bañar() en la clase ninja.
    def caminar(self):
        self.mascota.jugar()
        return self

    def alimentar(self):
        self.mascota.comer()
        return self

    def bañar(self):
        self.mascota.sonido()
        return self

    def mostrar_info(self):
        self.mascota.mostrar_info_mascota()
        return self

# Crea una instancia de un Ninja y asígnale una instancia de mascota al atributo de mascota.
jose = Ninja('Jose', 'Sepulveda', 'Master Dog')

# Haz que el ninja alimente, pasee y bañe a su mascota.
# jose.alimentar().caminar().bañar().mostrar_info()
jose.mostrar_info()
jose.caminar().alimentar().bañar()