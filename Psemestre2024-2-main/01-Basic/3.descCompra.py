precio_original = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))

descuento_cantidad = precio_original * (descuento / 100)
precio_conDescuento = precio_original - descuento_cantidad
IMPUESTO = 0.19
vImpuesto = precio_conDescuento * IMPUESTO
precio_final = precio_conDescuento + vImpuesto

print("El precio original es:", precio_original)
print("El descuento es de:", descuento_cantidad)
print("El precio con descuento es:", precio_conDescuento)
print("El impuesto es de:", vImpuesto)
print("El precio con impuesto es:", precio_final)
