class Figura3D:
    def calcular_volumen(self):
        print("Método no implementado.")

class Cubo(Figura3D):
    def __init__(self, lado):
        self.lado = lado

    def calcular_volumen(self):
        return self.lado ** 3

class Esfera(Figura3D):
    def __init__(self, radio):
        self.radio = radio

    def calcular_volumen(self):
        return (4/3) * 3.1416 * (self.radio ** 3)

cubo1 = Cubo(3)
cubo2 = Cubo(5)
cubo3 = Cubo(10)

esfera1 = Esfera(2)
esfera2 = Esfera(4)
esfera3 = Esfera(6)

print(f"Volumen del cubo1: {cubo1.calcular_volumen()} unidades cúbicas")
print(f"Volumen de la esfera1: {esfera1.calcular_volumen()} unidades cúbicas")

