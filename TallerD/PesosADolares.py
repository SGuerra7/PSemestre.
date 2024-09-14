precio_dolar = 4108.63
dolar = 4108.63
pesos = float(input("Ingrese cantidad en Pesos: "))

def pesos_a_dolares():
    convercion = pesos / precio_dolar
    print(f" El valor en Pesos convertido a Dolares es: {convercion}")

pesos_a_dolares()