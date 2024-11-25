class TransportePublico:
    def __init__(self, tipo, capacidad):
        self.tipo = tipo
        self.capacidad = capacidad

    def mostrar_info(self):
        print(f"Tipo de Transporte: {self.tipo}, Capacidad: {self.capacidad} pasajeros")

class Autobus(TransportePublico):
    def __init__(self, tipo, capacidad, ruta):
        super().__init__(tipo, capacidad)
        self.ruta = ruta

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Ruta: {self.ruta}")

class Tren(TransportePublico):
    def __init__(self, tipo, capacidad, numero_vagones):
        super().__init__(tipo, capacidad)
        self.numero_vagones = numero_vagones

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de Vagones: {self.numero_vagones}")

autobus1 = Autobus("Autobús Urbano", 50, "Ruta 1")
autobus2 = Autobus("Autobús Interurbano", 40, "Ruta 2")
autobus3 = Autobus("Autobús Escolar", 30, "Ruta 3")

tren1 = Tren("Tren de Cercanías", 200, 8)
tren2 = Tren("Tren Regional", 300, 12)
tren3 = Tren("Tren de Alta Velocidad", 400, 16)

autobus1.mostrar_info()
tren1.mostrar_info()
