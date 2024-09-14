salario = float(1300000)
def definir_salario():
    salario_actual = salario
    confirmacion_salario = int(input(" I"))
    print(f" El salario actual es: {salario}")
    print(" Por favor confirme sí actualmente persiste el mismo valor del salario.")
    print()


incremento = 4.2 / 100

def nuevo_salario():
    calculo_incremento = salario * incremento
    incremento_aplicado = salario + calculo_incremento
    print(f" El incremento para el proximo a es : {calculo_incremento:.2f} Pesos")
    print(f" El salario final para el proximo año es {incremento_aplicado} ")

nuevo_salario()