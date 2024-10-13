def contar_vocales(texto):  # Define la función 'contar_vocales' que recibe un parámetro 'texto'.

    texto = texto.lower()  # Convierte el 'texto' a minúsculas para que la búsqueda de vocales no distinga
    # entre mayúsculas y minúsculas.

    vocales = 'aeiou'  # Define un string que contiene las vocales a buscar.

    # Crea un diccionario con las vocales como claves y 0 como valor inicial para cada vocal.
    conteo = {vocal: 0 for vocal in vocales}

    # Recorre cada letra del texto ingresado.
    for letra in texto:
        # Si la letra es una vocal, actualiza el conteo de esa vocal en el diccionario.
        if letra in vocales:
            conteo[letra] += 1  # Incrementa el conteo de la vocal encontrada en 1.

    return conteo  # Devuelve el diccionario con el conteo de cada vocal.


# Solicita al usuario que ingrese una palabra o frase.
palabra = input("Ingrese una palabra o frase: ")

# Llama a la función 'contar_vocales' con el texto ingresado y almacena el resultado en 'resultado'.
resultado = contar_vocales(palabra)

print("Conteo de vocales:")  # Imprime el encabezado para mostrar el conteo.
# Recorre los pares vocal-cantidad en el diccionario 'resultado' y los imprime.
for vocal, cantidad in resultado.items():
    print(f"{vocal}: {cantidad}")