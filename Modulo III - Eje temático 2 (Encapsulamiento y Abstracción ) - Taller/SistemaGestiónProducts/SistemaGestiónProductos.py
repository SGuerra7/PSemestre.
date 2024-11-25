class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def ajustar_inventario(self, cantidad_cambio):
        self.cantidad += cantidad_cambio

    def mostrar_informacion(self):
        print(f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}")

art1 = Producto('Agua', 2000, 30)
art2 = Producto('Limonada', 2500, 20)
art3 = Producto('Tampico', 1300, 10)

art1.actualizar_precio(2200)
art2.ajustar_inventario(-20)
art3.mostrar_informacion()