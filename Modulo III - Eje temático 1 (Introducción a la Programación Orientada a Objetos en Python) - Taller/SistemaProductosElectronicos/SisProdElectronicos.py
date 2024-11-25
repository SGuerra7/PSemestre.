class ProductoElectronico:
    def __init__(self, nombre, precio, marca):
        self.nombre = nombre
        self.precio = precio
        self.marca = marca

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Precio: ${self.precio}, Marca: {self.marca}")

class TelefonoMovil(ProductoElectronico):
    def __init__(self, nombre, precio, marca, capacidad_bateria):
        super().__init__(nombre, precio, marca)
        self.capacidad_bateria = capacidad_bateria

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Capacidad de Batería: {self.capacidad_bateria} mAh")

class Laptop(ProductoElectronico):
    def __init__(self, nombre, precio, marca, tamano_pantalla):
        super().__init__(nombre, precio, marca)
        self.tamano_pantalla = tamano_pantalla

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tamaño de Pantalla: {self.tamano_pantalla} pulgadas")

telefono1 = TelefonoMovil("Galaxy S23", 999, "Samsung", 4500)
telefono2 = TelefonoMovil("iPhone 15", 1299, "Apple", 4300)
telefono3 = TelefonoMovil("Pixel 8", 799, "Google", 4600)

laptop1 = Laptop("MacBook Air", 1199, "Apple", 13.6)
laptop2 = Laptop("Dell XPS", 999, "Dell", 15.0)
laptop3 = Laptop("HP Spectre", 899, "HP", 14.0)

telefono1.mostrar_info()
laptop1.mostrar_info()
