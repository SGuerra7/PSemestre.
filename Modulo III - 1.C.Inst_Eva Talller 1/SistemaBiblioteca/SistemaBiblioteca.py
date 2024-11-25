class MaterialBiblioteca:
    def __init__(self, titulo, autor, codigo):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"{self.titulo} ha sido prestado.")
        else:
            print(f"{self.titulo} no está disponible.")

    def devolver(self):
        self.disponible = True
        print(f"{self.titulo} ha sido devuelto.")

    def mostrar_info(self):
        estado = "Disponible" if self.disponible else "No disponible"
        print(f"Título: {self.titulo}, Autor: {self.autor}, Código: {self.codigo}, Estado: {estado}")

class Libro(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigo, numero_paginas, genero):
        super().__init__(titulo, autor, codigo)
        self.numero_paginas = numero_paginas
        self.genero = genero

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de Páginas: {self.numero_paginas}, Género: {self.genero}")

class Revista(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigo, numero_edicion, fecha_publicacion):
        super().__init__(titulo, autor, codigo)
        self.numero_edicion = numero_edicion
        self.fecha_publicacion = fecha_publicacion

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de Edición: {self.numero_edicion}, Fecha de Publicación: {self.fecha_publicacion}")

libro1 = Libro("El Quijote", "Miguel de Cervantes", "L001", 863, "Ficción")
libro2 = Libro("1984", "George Orwell", "L002", 328, "Distopía")
libro3 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "L003", 471, "Realismo Mágico")

revista1 = Revista("National Geographic", "Varios", "R001", 55, "2024-01")
revista2 = Revista("TIME", "Varios", "R002", 34, "2024-02")
revista3 = Revista("Scientific American", "Varios", "R003", 20, "2024-03")

libro1.mostrar_info()
libro1.prestar()
libro1.mostrar_info()
libro1.devolver()
libro1.mostrar_info()

revista1.mostrar_info()
