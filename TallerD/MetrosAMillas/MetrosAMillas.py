
from colorama import Fore, Style, init
init()

def convertir_metros_millas():
    print(Fore.LIGHTGREEN_EX + "Vamos a convertir la longitud en metros a millas!" + Style.RESET_ALL)
    while True:
        entrada = input(Fore.GREEN + " Ingrese cantidad en metros: " + Style.RESET_ALL)
        try:
            metros = float(entrada)
            break
        except ValueError:
            print(Fore.RED + " Error: Digíte un nùmero válido." + Style.RESET_ALL)

    millas = metros / 1609.343
    print(f" La longitud en metros = {metros} en millas es: {millas}")


def menu_opcion_continuar():
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
    convertir_metros_millas()
    if not menu_opcion_continuar():
        print(Fore.YELLOW + "Gracias por utilizar el script" + Style.RESET_ALL)