def menu_destinos():
    print("Seleccione lugar de destino: ")
    print("1. Estados Unidos ")
    print("2. Canadá ")
    print("3. Europa ")
    print("4. Resto del Mundo ")


menu_destinos()


OpcionDestinos = input("Ingrese el número correspondiente al lugar de destino: ")
CantidadMinutos = float(input("Ingrese duración en minutos: "))
DESCUENTO = 0.20


def estadosunidos():
    return 900 * CantidadMinutos


def canada():
    return 800 * CantidadMinutos


def europa():
    return 950 * CantidadMinutos


def resto_del_mundo():
    return 1250 * CantidadMinutos


def descuento_aplicado():
    return CostoTotal * (1 - DESCUENTO)


if OpcionDestinos == "1":
    print("Haz Seleccionado Estados Unidos")
    print(f"Costo total de la llamada:  {estadosunidos()}")
    CostoTotal = estadosunidos()
elif OpcionDestinos == "2":
    print("Haz Seleccionado Canadá")
    print(f"Costo total de la llamada:  {canada()}")
elif OpcionDestinos == "3":
    print("Haz Seleccionado Europa")
    print(f"Costo total de la llamada:  {europa()}")
elif OpcionDestinos == "4":
    print("Haz Seleccionado Resto del mundo")
    print(f"Costo total de la llamada:  {resto_del_mundo()}")
elif CantidadMinutos >= 15:
    print(f"Costo total de la llamada con descuentos es: {descuento_aplicado()}")
else:
    print("Error, Digite un número Valido")
