from datetime import datetime



class Coche:

    def __init__(self, marca, modelo, anio):
        # Atributo de instancia (propio de cada objeto)
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def descripcion(self):
        return f"{self.marca} - {self.modelo} - {self.anio}"

    def es_antiguo(self):

        aino_actual = datetime.now().year
        return (aino_actual - self.anio) > 10


    def __str__(self):
        return f"{self.marca} - {self.modelo} - {self.anio}"



# Pruebas
coche = Coche("Seat", "León", 2015)
print(coche.descripcion())   # Seat León (2015)
print(coche.es_antiguo())    # True

coche2 = Coche("Tesla", "Model 3", 2023)
print(coche2.descripcion())  # Tesla Model 3 (2023)
print(coche2.es_antiguo())   # False