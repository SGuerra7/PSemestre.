def filtrar_palabras(): # Se crea la función
    palabras = [] # Se crea una lista vacía que alojará las palabras,
    while True: # Bucle condicional, mientras la palabra contenga letras el bucle continua.
        palabra = input("Ingrese una palabra (o presione Enter para terminar): ") # Petición al usuario de la palabra.
        if palabra == "": # Condicional que define si la palabra esta vacía, el bucle termina.
            break # Para terminar el bucle.
        palabras.append(palabra) # Una vez se digíte la palabra esta se envía a la lista 'palabras'.

    letra = input("Ingrese la letra inicial para filtrar: ").lower() # Petición al usuario para ingresar letra, por la
    # cual se filtrarán las palabras que comienzan por la letra indicada.

    print(f"\nPalabras que comienzan con '{letra}':") # Llamada a imprimir un encabezado junto con la letra indicada.
    for palabra in palabras: #Bucle for, que recorre las palabras.
        if palabra.lower().startswith(letra): # Condicional que verifica sí la palabra empieza por la letra indicada.
            # Aqui '.lower' convierte toda la palabra en minusculas y ',startwith()' es una función preestablecida para
            # determinar sí la 'palabra' empieza por 'letra'.
            print(palabra) # Imprime las palabras filtradas.


filtrar_palabras()