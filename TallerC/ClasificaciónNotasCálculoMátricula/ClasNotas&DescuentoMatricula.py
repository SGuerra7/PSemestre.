from colorama import Fore, Style, init
init()

DESCUENTO: float= 0.20

def calcular_promedio():
    print(Fore.YELLOW + "Vamos a calcular el promedio de las notas!" + Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX + "Ingrese valores entre 1 - 5" + Style.RESET_ALL)
    while True:
        notas = []
        for i in range (4):
            while True:
                try:
                    nota = float(input(f" Ingrese nota {i + 1}: "))
                    if 1 <= nota <= 5:
                        notas.append(nota)
                        break
                    else:
                        print(Fore.RED + "Por favor ingrese valores entre 1 y 5" + Style.RESET_ALL)
                except ValueError:
                    print(Fore.RED + " Entrada no válida, ingrese un número." + Style.RESET_ALL)

        promedio = sum(notas) / len(notas)
        print(f"El promedio de las notas es: {Fore.LIGHTCYAN_EX}{promedio}{Style.RESET_ALL}" )

        if 4 <= promedio <= 5 :
            print(f"El rendimiento es: {Fore.LIGHTGREEN_EX}Excelente{Style.RESET_ALL}")
        elif 3 <= promedio <= 3.99:
            print(f"El rendimiento es: {Fore.GREEN}Bueno{Style.RESET_ALL}")
        elif 0 <= promedio <= 2.99:
            print(f"El rendimiento es: {Fore.RED}Deficiente{Style.RESET_ALL}")
        else:
            print(Fore.RED + "Error, Promedio Invalido." + Style.RESET_ALL)
        return promedio


def calcular_matricula(promedio):

    while True:
        entrada = input("Ingrese el costo de matrícula: ")
        try:
            costo_matricula = float(entrada)
            break
        except ValueError:
            print(Fore.RED + "Error: Ingrese un valor númerico valido." + Style.RESET_ALL)


    if 4 <= promedio <= 5:
        matricula_con_descuento = costo_matricula * (1 - DESCUENTO)
        print(f"El valor de la matrícula con descuento es: {Fore.LIGHTCYAN_EX}{matricula_con_descuento}"
              f"{Style.RESET_ALL}")
        return matricula_con_descuento
    else:
        print(Fore.MAGENTA + "El descuento no aplica a tu promedio." + Style.RESET_ALL)
        return costo_matricula


def menu_opcion_retornar():
    while True:
        print(Fore.CYAN +  " ¿Realizar otro cálculo? " + Style.RESET_ALL)
        print("1. Si")
        print("2. No")
        opcion_menu = (input("Ingrese número de opción válido: "))
        if opcion_menu == "1":
            return True
        elif opcion_menu == "2":
            return False
        else:
            print(Fore.RED + "Digíte un número válido." + Style.RESET_ALL)


while True:
    promd = calcular_promedio()
    calcular_matricula(promd)
    if not menu_opcion_retornar():
        print(Fore.LIGHTBLUE_EX + "Gracias por utilizar el script ;)" + Style.RESET_ALL)
        break