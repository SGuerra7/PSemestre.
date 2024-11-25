class Estudiante:
    def __init__(self, nombre, edad, grado, materias=None):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.materias = materias if materias else []

    def inscribir_materia(self, materia):
        self.materias.append(materia)

    def mostrar_materias(self):
        print(f"{self.nombre} está inscrito en: {', '.join(self.materias)}")

    def actualizar_grado(self, nuevo_grado):
        self.grado = nuevo_grado

estudiante1 = Estudiante("Juan", 16, "10°")
estudiante2 = Estudiante("María", 15, "9°")
estudiante3 = Estudiante("Carlos", 17, "11°")

estudiante1.inscribir_materia("Matemáticas")
estudiante2.actualizar_grado("10°")
estudiante3.inscribir_materia("Español"), estudiante3.mostrar_materias()
