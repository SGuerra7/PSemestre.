
listanumeros = []

def suma_pares(lista):
    suma = 0
    while True:
        try:
            numero = int(input("Ingrese número para agregar a la lista (Digíte 0 para finalizar):  "))
            listanumeros.append(numero)
            if numero == 0:
                break
        except ValueError:
            print("Error: Digíte un número valido.")
    for numero in listanumeros:
        if numero % 2 == 0:
            suma += numero
    return suma

resultado = suma_pares(listanumeros)
print(f'La suma de los números pares es: {resultado}')