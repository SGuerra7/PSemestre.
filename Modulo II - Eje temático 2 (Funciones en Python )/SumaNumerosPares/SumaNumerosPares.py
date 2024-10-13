def sumar_pares():
    numeros = []
    while True:
        try:
            num = input("Ingrese un número (o presione Enter para terminar): ")
            if num == "":
                break
            numeros.append(int(num))
        except ValueError:
            print("Por favor, ingrese un número válido.")

    suma_pares = 0
    for numero in numeros:
        if numero % 2 == 0:
            suma_pares += numero

    print(f"\nLa suma de los números pares es: {suma_pares}")


sumar_pares()