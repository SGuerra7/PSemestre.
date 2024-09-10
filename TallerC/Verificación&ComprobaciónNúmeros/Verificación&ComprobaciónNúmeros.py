x, y, z, w = 15, 10, 20, 8
"""Verifica si 'x' está entre 'y' y 'z', y si 'w' es par: """
if y < x < z and w % 2 == 0:
    print(f" x = {x} Está entre {y} y {z}. y = {w} Por lo tanto, es par.")
else:
    print(f"{x} No está entre {y} y {z}. y = {w} No es par.")


a, b, c, d = 7, 5, 3, 3
"""Comprueba si 'a' es mayor que 'b' o si 'c' es igual a 'd', pero no ambas """
if a > b or c == d:
    print(f" a = {a} y b = {b}, 'a' es mayor que 'b'."
          f" c = {c} y d = {d}, 'c' y 'd' son iguales. ")
else:
    print(" Ninguna de las condiciones se cumple.")


x, y, z = -3, 5, 0
"""Verifica si 'x' es negativo, 'y' es positivo, y 'z' es cero: """
if x < 0 < y and z == 0:
    print(f" x = {x} Por lo tanto, es negativo. "
          f" y = {y} Por lo tanto, es positivo. "
          f" z = {z} Por lo tanto, es igual a 0.")
else:
    print(f" x = {x} Por lo tanto, no es negativo. "
          f" y = {y} Por lo tanto, no es positivo. "
          f" z = {z} Por lo tanto, no es igual a 0.")