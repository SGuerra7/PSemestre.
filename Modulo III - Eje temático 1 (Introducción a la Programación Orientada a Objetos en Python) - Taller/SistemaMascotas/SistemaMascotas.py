class Mascota:
    def __init__(self, nombre, edad, especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Especie: {self.especie}")

class Perro(Mascota):
    def __init__(self, nombre, edad, especie, raza):
        super().__init__(nombre, edad, especie)
        self.raza = raza

    def ladrar(self):
        print("Guau, guau")

class Gato(Mascota):
    def __init__(self, nombre, edad, especie, color):
        super().__init__(nombre, edad, especie)
        self.color = color

    def maullar(self):
        print("Miau")

perro1 = Perro("Max", 3, "Perro", "Golden Retriever")
perro2 = Perro("Buddy", 5, "Perro", "Beagle")
perro3 = Perro("Rocky", 2, "Perro", "Labrador")

gato1 = Gato("Luna", 4, "Gato", "Blanco")
gato2 = Gato("Milo", 2, "Gato", "Negro")
gato3 = Gato("Simba", 3, "Gato", "Gris")

perro1.mostrar_info()
perro2.mostrar_info()
gato1.mostrar_info()
gato3.mostrar_info()

perro1.ladrar()
gato1.maullar()
