def eliminar_duplicados(lista):
    elementos_vistos = set()
    resultado = []
    for elemento in lista:
        if elemento not in elementos_vistos:
            elementos_vistos.add(elemento)
            resultado.append(elemento)
    return resultado

lista_original = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 9, 10  ]
lista_sin_duplicados = eliminar_duplicados(lista_original)
print(f"Lista original: {lista_original}")
print(f"Lista sin duplicados: {lista_sin_duplicados}")