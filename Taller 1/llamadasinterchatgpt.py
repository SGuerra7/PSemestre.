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

def estadosunidos(minutos):
    return 900 * minutos

def canada(minutos):
    return 800 * minutos

def europa(minutos):
    return 950 * minutos

def resto_del_mundo(minutos):
    return 1250 * minutos

def aplicar_descuento(costo_total):
    return costo_total * (1 - DESCUENTO)

if OpcionDestinos == "1":
    print("Has seleccionado Estados Unidos")
    CostoTotal = estadosunidos(CantidadMinutos)
elif OpcionDestinos == "2":
    print("Has seleccionado Canadá")
    CostoTotal = canada(CantidadMinutos)
elif OpcionDestinos == "3":
    print("Has seleccionado Europa")
    CostoTotal = europa(CantidadMinutos)
elif OpcionDestinos == "4":
    print("Has seleccionado Resto del Mundo")
    CostoTotal = resto_del_mundo(CantidadMinutos)
else:
    print("Error, digite un número válido")
    CostoTotal = 0  # Para manejar el caso en el que la opción es inválida

if CostoTotal > 0:
    if CantidadMinutos >= 15:
        CostoTotalConDescuento = aplicar_descuento(CostoTotal)
        print(f"Costo total de la llamada con descuento es: {CostoTotalConDescuento}")
    else:
        print(f"Costo total de la llamada es: {CostoTotal}")
