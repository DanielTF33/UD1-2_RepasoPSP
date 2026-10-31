from datetime import datetime


class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def descripcion(self):
        return f"Marca: {self.marca} - Modelo: {self.modelo} - Año:{self.año}"

    def es_antiguo(self):
        año_actual = datetime.now().year
        return (año_actual - self.año) > 10


coche = Coche("Seat", "León", 2015)
print(coche.descripcion())   # Seat León (2015)
print(coche.es_antiguo())    # True

coche2 = Coche("Pepega", "Leon", 2034)
print(coche2.descripcion())
print(coche2.es_antiguo())