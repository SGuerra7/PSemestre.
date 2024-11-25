class Vehiculo:
    def __init__(self, marca, modelo, año, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje

    def conducir(self, kilometros):
        self.kilometraje += kilometros

    def mostrar_detalles(self):
        print(f"Vehículo: {self.marca} {self.modelo}, Año: {self.año}, Kilometraje: {self.kilometraje}")

    def es_vehiculo_antiguo(self):
        return (2024 - self.año) > 20

vehiculo1 = Vehiculo("Toyota", "Corolla", 2000, 150000)
vehiculo2 = Vehiculo("Ford", "Fiesta", 2018, 40000)
vehiculo3 = Vehiculo("Honda", "Civic", 1995, 200000)

vehiculo1.conducir(500), vehiculo1.mostrar_detalles()
vehiculo2.mostrar_detalles()
print(vehiculo3.es_vehiculo_antiguo())
