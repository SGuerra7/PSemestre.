class Factura:
    def __init__(self, numero, cliente, fecha, monto_total=0):
        self.numero = numero
        self.cliente = cliente
        self.fecha = fecha
        self.monto_total = monto_total
        self.items = []

    def agregar_item(self, descripcion, cantidad, precio_unitario):
        subtotal = cantidad * precio_unitario
        self.items.append((descripcion, cantidad, precio_unitario, subtotal))
        self.monto_total += subtotal

    def aplicar_descuento(self, porcentaje):
        self.monto_total -= self.monto_total * (porcentaje / 100)

    def mostrar_detalles(self):
        print(f"Factura {self.numero} para {self.cliente}, Fecha: {self.fecha}")
        for item in self.items:
            print(f"- {item[0]} x{item[1]}: {item[3]}$")
        print(f"Monto Total: {self.monto_total}$")

factura1 = Factura(1, "Juan Pérez", "2024-11-23")
factura1.agregar_item("Laptop", 1, 1200)
factura1.agregar_item("Mouse", 2, 25)

factura1.aplicar_descuento(5)
factura1.mostrar_detalles()
