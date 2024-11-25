class VehiculoCarreras:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Velocidad Máxima: {self.velocidad_maxima}")

class CocheF1(VehiculoCarreras):
    def __init__(self, marca, modelo, velocidad_maxima, tipo_neumaticos):
        super().__init__(marca, modelo, velocidad_maxima)
        self.tipo_neumaticos = tipo_neumaticos

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de Neumáticos: {self.tipo_neumaticos}")

class MotoGP(VehiculoCarreras):
    def __init__(self, marca, modelo, velocidad_maxima, tipo_carenado):
        super().__init__(marca, modelo, velocidad_maxima)
        self.tipo_carenado = tipo_carenado

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de Carenado: {self.tipo_carenado}")

coche1 = CocheF1("Ferrari", "SF23", 350, "Intermedias")
coche2 = CocheF1("Mercedes", "W14", 340, "Suaves")
coche3 = CocheF1("Red Bull", "RB19", 360, "Medias")

moto1 = MotoGP("Yamaha", "YZR-M1", 300, "Tipo A")
moto2 = MotoGP("Ducati", "Desmosedici GP23", 310, "Tipo B")
moto3 = MotoGP("Honda", "RC213V", 320, "Tipo C")

coche1.mostrar_info()
moto1.mostrar_info()
