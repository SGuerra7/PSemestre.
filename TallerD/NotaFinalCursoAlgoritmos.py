
from colorama import Fore, Style, init
init()


TALLER1: float = (20 / 100)
TALLER2: float = (15 / 100)
CUSTIONARIO1: float = (22 / 100)
CUSTIONARIO2: float = (10 / 100)
PROYECTOFINAL: float = (33 / 100)


def notas_input():
    print(Fore.LIGHTBLUE_EX + "Vamos a calcular la nota final del curso Fundamentos de Algoritmos!" + Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "Ingrese las notas del 1.0 a 5.0 correspondientes a cada actividad: "+ Style.RESET_ALL)
    while True:
        notas = []
        for i in range (5):
            while True:
                try:
                    nota = float(input(f" Ingrese la nota {i + 1}: " ))
                    if 1 <= nota <= 5:
                        notas.append(nota)
                        break
                    else:
                        print(Fore.RED + "Error: Ingrese valores de 1.0 a 5.0" + Style.RESET_ALL)
                except ValueError:
                    print(Fore.RED + " Entrada no valida, ingrese un valor númerico." + Style.RESET_ALL)

        notas_final = ((notas[0] * TALLER1) + (notas[1] * TALLER2) + (notas[2] * CUSTIONARIO1) +
                       (notas[3] * CUSTIONARIO2) + (notas[4] * PROYECTOFINAL) )
        print( f" La nota final del curso es: {Fore.LIGHTMAGENTA_EX}{notas_final:.2f}{Style.RESET_ALL}" )

        if 4.5 <= notas_final <= 5:
            print(f" Tu desempeño en el curso fue: {Fore.LIGHTGREEN_EX}Excelente{Style.RESET_ALL}")
        elif 3.5 <= notas_final <= 4.49:
            print(f" Tu desempeño en el curso fue: {Fore.GREEN}Bueno{Style.RESET_ALL}")
        elif 3.0 <= notas_final <= 3.49:
            print(f" Tu desempeño en el curso fue: {Fore.BLUE}Regular{Style.RESET_ALL}")
        elif 1 <= notas_final <= 2.99:
            print(f" Tu desempeño en el curso fue: {Fore.RED}Deficiente{Style.RESET_ALL}")
        else:
            print(Fore.RED + "Cálculo inválido" + Style.RESET_ALL)
        return



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
    notas_input()
    if not menu_opcion_retornar():
        print(Fore.LIGHTBLUE_EX + "Gracias por utilizar el script ;)" + Style.RESET_ALL)
        break
