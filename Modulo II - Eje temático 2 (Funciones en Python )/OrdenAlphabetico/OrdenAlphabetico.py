def ordenar_nombres():
    nombres = []
    while True:
        nombre = input("Ingrese un nombre (o presione Enter para terminar): ")
        if nombre == "":
            break
        nombres.append(nombre)

    nombres_ordenados = sorted(nombres)

    print("\nLista de nombres en orden alfabético:")
    for nombre in nombres_ordenados:
        print(nombre)

ordenar_nombres()