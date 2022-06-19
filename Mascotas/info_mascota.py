# 1. Crea una clase Mascota con los atributos mascota mencionados anteriormente.
class Mascota:

    def __init__(self, nombre, tipo, golosinas, salud, energia):
        self.nombre = nombre
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = salud
        self.energia = energia

    # Implementa dormir(), comer(), jugar(), sonido() en la clase mascota.
    def dormir(self):
        self.energia += 25
        print(f'salud: {self.salud}')
        print(f'energía: {self.energia}')
        return self

    def comer(self):
        self.energia += 5
        self.salud += 10
        print(f'salud: {self.salud}')
        print(f'energía: {self.energia}')
        return self

    def jugar(self):
        self.salud += 5
        print(f'salud: {self.salud}')
        print(f'energía: {self.energia}')
        return self

    def sonido(self):
        print('Guau guau!')
        return self

    def mostrar_info_mascota(self):
        print(f'nombre: {self.nombre} - tipo: {self.tipo} - golosinas: {self.golosinas} - salud:{self.salud} - energía: {self.energia}')
        return self