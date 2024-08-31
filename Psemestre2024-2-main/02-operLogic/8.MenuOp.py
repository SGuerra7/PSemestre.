nombre = input("Ingrese Nombre:")
edad = int(input("Ingrese Edad:"))

if edad >= 18:
    print(F"{nombre} tienes {edad} años. Por lo tanto puedes votar")
else:
    print(f"{nombre} tienes {edad} años. Por lo tanto no puedes votar")

