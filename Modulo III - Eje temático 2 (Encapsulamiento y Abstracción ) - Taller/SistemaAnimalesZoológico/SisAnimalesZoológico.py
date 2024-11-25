class Animal:
    def __init__(self, nombre, especie, edad, habitat):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.habitat = habitat

    def cumplir_años(self):
        self.edad += 1

    def cambiar_habitat(self, nuevo_habitat):
        self.habitat = nuevo_habitat

    def mostrar_detalles(self):
        print(f"Animal: {self.nombre}, Especie: {self.especie}, Edad: {self.edad}, Hábitat: {self.habitat}")

animal1 = Animal("Simba", "León", 5, "Sabana")
animal2 = Animal("Manny", "Elefante", 10, "Selva")
animal3 = Animal("Gloria", "Hipopótamo", 7, "Río")

animal1.cumplir_años()
animal2.cambiar_habitat("Reserva")
animal3.mostrar_detalles()
