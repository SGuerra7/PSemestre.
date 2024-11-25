class Habitacion:
    def __init__(self, numero, tipo, precio, disponible=True):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = disponible

    def reservar(self):
        self.disponible = False

    def liberar(self):
        self.disponible = True

    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "Ocupada"
        print(f"Habitación {self.numero}: {self.tipo}, Precio: {self.precio}, Estado: {estado}")

habitacion1 = Habitacion(101, "Individual", 50)
habitacion2 = Habitacion(102, "Doble", 75)
habitacion3 = Habitacion(103, "Suite", 150)

habitacion1.reservar()
habitacion2.mostrar_informacion()
habitacion3.liberar()
