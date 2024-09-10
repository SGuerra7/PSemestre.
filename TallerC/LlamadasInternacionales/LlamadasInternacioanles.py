from colorama import Fore, Style, init
init()

DESCUENTO: float = 0.20

def funcion_principal(): # Esta función contiene todas las funciónes para realizar el cálculo principal.

    def menu_destinos():  # Se define función para desplegar el menú.
        print(Fore.LIGHTBLUE_EX + "Seleccione lugar de destino: " + Style.RESET_ALL)
        print("1. Estados Unidos ")
        print("2. Canadá ")
        print("3. Europa ")
        print("4. Resto del Mundo ")

    """
    # Se define el bucle sobre las variables a ingresar, para cuando se elija una opción correcta, el bucle se detiene.
    # y cuando se elija una opción incorrecta, el bucle vuelva a desplegar el menú, no sin antes  mostrar
    # un mensaje de alerta en color rojo. Aqui use la biblioteca Colorama. Las modificaciónes de color en Colorama
    se escriben como `Fore.GREEN + "Texto a modificar" + Style.RESET_ALL`.
    """

    while True:
        menu_destinos()  # Se llama a la funcion del menú.
        opcion_destinos = input("Ingrese el número correspondiente al lugar de destino: ")

        if opcion_destinos == "1":
            print(Fore.GREEN + "Has seleccionado Estados Unidos" + Style.RESET_ALL)
            print(Fore.GREEN + " 900 Pesos * Minuto" + Style.RESET_ALL)
            break
        elif opcion_destinos == "2":
            print(Fore.GREEN + "Has seleccionado Canadá" + Style.RESET_ALL)
            print(Fore.GREEN + " 800 Pesos * Minuto" + Style.RESET_ALL)
            break
        elif opcion_destinos == "3":
            print(Fore.GREEN + "Has seleccionado Europa" + Style.RESET_ALL)
            print(Fore.GREEN + " 950 Pesos * Minuto" + Style.RESET_ALL)
            break
        elif opcion_destinos == "4":
            print(Fore.GREEN + "Has seleccionado Resto del Mundo" + Style.RESET_ALL)
            print(Fore.GREEN + " 1.250 Pesos * Minuto" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Error, digite un número válido." + Style.RESET_ALL)
            continue

# variable de tipo input/float, para una llamada a pedir los datos, con condicional por si registra un dato tipo string.
    while True:
        entrada = input("Ingrese duración en minutos: ")
        try:
            cantidad_minutos = float(entrada)
            break
        except ValueError:
            print(Fore.RED + "Error: Ingrese un valor numérico válido." + Style.RESET_ALL)


# funciones para cada lugar, que contine un calculo entre el preecio y la cantidad de minutos.
    def estadosunidos(minutos): # Para cada opción se define una función.
        return 900 * minutos

    def canada(minutos):
        return 800 * minutos
    """
        El argumento "minutos" se enlaza con "cantidad_minutos" en los condicionales "opcion_destinos". Lineas 83 a 92.
        Su enlaze ocurre por la llamada a la función de cada lugar que tiene como argumento "cantidad_minutos"
    """

    def europa(minutos):
        return 950 * minutos

    def resto_del_mundo(minutos):
        return 1250 * minutos

# Función que aplica un descuento usando la variable global "DESCUENTO" .
    def aplicar_descuento(costototal):
        """
        Notese que el argumento "costototal" está escrito de manera diferente a la variable definida en los
        condicionales de "opción_destinos", en las lineas 85, 87, 89, 91 y 93.
         Sin embargo Python enlaza este argumento al argumento en llamada a los
        condicionales  "costo_total" que se encuentra en la linea 95, en la definición de la variable
        "costo_total_con_descuento" y dentro del argumento de la función "aplicar_descuento".
        Es decir aplica la función "aplicar_descuento" al argumento "costo_total" que es una variable que se define
        en cada condicional de "opción_destinos" en las lineas 84 a 93.
        """
        return costototal * (1 - DESCUENTO) # Lo hace de manera que resta el porcentaje de descuento a 1
        # lo cual es = 0.80. Después se multiplica el "costotal" por el resultado de la resta, y esto nos devuelve
        # el valor de la llamada con el descuento aplicado.

    def calcular_descuento(costotal): # Esta función cálcula el descuento que se le hará al precio de la llamada.
        # Esto lo hago para que el usuario se informe cuanto se le descuenta, se imprime en la linea 111.
        return costotal * DESCUENTO

# Condicionales que definen la variable "costo_total" al registrar el input de "opcion_destinos".
    if opcion_destinos == "1":
        costo_total = estadosunidos(cantidad_minutos)
    elif opcion_destinos == "2":
        costo_total = canada(cantidad_minutos)
    elif opcion_destinos == "3":
        costo_total = europa(cantidad_minutos)
    elif opcion_destinos == "4":
        costo_total = resto_del_mundo(cantidad_minutos)
    else:
        costo_total = 0  # Para manejar el caso en el que la opción es inválida

# Condicionales que imprimen los valores de los calculos, además aplica el descuento si son mas de 15 minutos.
    if costo_total > 0:
        if cantidad_minutos >= 15:
            costo_total_con_descuento = aplicar_descuento(costo_total)
            print(f"{Fore.LIGHTRED_EX}✦{Style.RESET_ALL} Costo total de la llamada es: {Fore.LIGHTBLUE_EX}{costo_total}"
                  f" Pesos {Style.RESET_ALL}")
            print(f"{Fore.LIGHTRED_EX}✦{Style.RESET_ALL}  Descuento por cantidad de minutos mayor o igual a 15 es: "
                  f"{Fore.LIGHTBLUE_EX}{calcular_descuento(costo_total)} Pesos{Style.RESET_ALL}")
            print(f"{Fore.LIGHTRED_EX}✦{Style.RESET_ALL}   Costo total de la llamada con descuento es: "
                  f"{Fore.LIGHTBLUE_EX}{costo_total_con_descuento} Pesos{Style.RESET_ALL}")
        else:
            print(f"{Fore.LIGHTRED_EX}✦{Style.RESET_ALL} Costo total de la llamada es: {Fore.LIGHTBLUE_EX}{costo_total}"
                  f"{Style.RESET_ALL} Pesos")
    else:
        print(f"El costo total de la llamada es: {Fore.LIGHTBLUE_EX}{costo_total}{Style.RESET_ALL} Pesos")


def menu_opcion_continuar(): # Esta función imprime un menú que nos indica sí queremos volver a realizar un calculo.
    while True:
        print(Fore.CYAN + "¿Realizar otro cálculo?" + Style.RESET_ALL)
        print("1. Si")
        print("2. No")
        continuar = (input(" Ingrese el número de la opción correspondiente: "))
        if continuar == "1":
            return True
        elif continuar == "2":
            return False
        else:
            print(Fore.RED + "Error, digite un número valido." + Style.RESET_ALL)


while True:
    """
    Este bucle nos permite mantenernos en bucle ejecutando la función principal para volver a hacer el calculo, 
    sí en el "menu_opcion_continuar" elejimos la opción "2. No" imprime un mensaje de finalización.
    """
    funcion_principal()
    if not menu_opcion_continuar():
        print(Fore.GREEN + "Gracias por utilizar el script ;)" + Style.RESET_ALL)
        break