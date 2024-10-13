def invertir_lista(lista):
    return lista[::-1] # "[::-1] Es una función predefinida en python, nos permite invertir la lista."


lista_original = [1, 2, 3, 4, 5]
lista_invertida = invertir_lista(lista_original)
print(f"Lista original: {lista_original}")
print(f"Lista invertida: {lista_invertida}")