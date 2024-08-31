montoInversion = float(input("Digite el monto: "))
T_ANUAL = float(input("Digite el porcentaje de interés anual:"))
T_Inversion = float(input("Digite el tiempo de duración en años"))

InteresDecimal = T_ANUAL / 100
T_InversionEnMeses = T_Inversion * 12
InteresSimple = montoInversion * InteresDecimal * T_Inversion
MontoFinal = montoInversion + InteresSimple

print("El interes simple es:", InteresSimple)
print("El total sumado al final de la inversión es:", MontoFinal)

