class Libro:
    def __init__(self, titulo, autor, genero, precio):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.precio = precio

    def aplicar_descuento(self, porcentaje):
        self.precio -= self.precio * (porcentaje / 100)

    def mostrar_informacion(self):
        print(f"Libro: {self.titulo}, Autor: {self.autor}, Género: {self.genero}, Precio: {self.precio}")

    def es_mas_caro_que(self, otro_libro):
        return self if self.precio > otro_libro.precio else otro_libro

libro1 = Libro("El Quijote", "Cervantes", "Novela", 20)
libro2 = Libro("1984", "Orwell", "Distopía", 15)
libro3 = Libro("Cien Años de Soledad", "García Márquez", "Realismo mágico", 25)

libro1.aplicar_descuento(10)
libro2.mostrar_informacion()
print(libro3.es_mas_caro_que(libro1).titulo)
