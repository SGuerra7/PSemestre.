def eliminar_duplicados(lista): #Se crea una función con el parametro "Lista"

    elementos_vistos = set() # Se define una lista con la función set, que no permite duplicados al definir un conjunto.

    resultado = [] # lista vacía que alojara elementos sin duplicados.

    for elemento in lista: # Bucle for para recorrer la lista.

        if elemento not in elementos_vistos: # Condicional que verifica si un elemento no esta en el conjunto set.
            # Sí no está envía este elemento a las siguientes listas:

            elementos_vistos.add(elemento) # A la lista 'elementos_vistos' se añade cada elemento que recorre el bucle.

            resultado.append(elemento) # Se envía cada elemento no visto a la lista vacía "Resultado"

            # Si el elemento está en 'elementos_vistos' no enviará el elemento a las anteriores listas.

    return resultado # Retorna la lista resultado con sus respectivos elementos.

lista_original = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 9, 10  ]
lista_sin_duplicados = eliminar_duplicados(lista_original)
print(f"Lista original: {lista_original}")
print(f"Lista sin duplicados: {lista_sin_duplicados}")