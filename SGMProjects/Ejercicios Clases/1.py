""""#a = 7

print(a)
Los comentarios multilinea están dentro de triples doble comilla."""

# Comentario de Linea Unica.

# Identación.
x = 10
y = 20
if x > y:
    print("X es mayor que y")
else:
    print("X es menor que y")

# Operadores Lógicos.

"""
Los operadores lógicos o logical operators nos 
permiten trabajar con valores de tipo booleano. 
Un valor booleano o bool es un tipo que solo 
puede tomar valores True o False. Por lo tanto,
 estos operadores nos permiten realizar diferentes 
 operaciones con estos tipos, y su resultado será 
 otro booleano. Por ejemplo, True and True usa el 
 operador and, y su resultado será True. 
 A continuación lo explicaremos mas en detalle.
 
 Operador	    Nombre	         Ejemplo
 
 and	        T T = T 	     True and True = True
 or             T F = T          True or False = True
 not            T = F            not True = False
"""

# Operadores de Asignación.

x = 2  # Uso correcto del operador =
print(x)  # 2
"""3=5      # Daría error, 3 no es una variable"""

""" 
Operador += 
omo podemos ver, todos los operadores de asignación 
no son más que atajos para escribir otros operadores 
de manera más corta, y asignar su resultado a la 
variable inicial. El operador += en x+=1 
es equivalente a x=x+1
"""
x = 5  # Ejemplo de como incrementar
x += 1  # en una unidad x
print(x)


# f-string

def saludar(nombre: object) -> object:
    """Esta función imprime un saludo."""
    print(f"Hola, {nombre}!")
    return object


# Llamada a la función
saludar("Juan")

# Operador **

"""El operador ** realiza el exponente del número
 a la izquierda elevado al número de la derecha."""

print(10 ** 3)  # 1000
print(2 ** 2)  # 4

"""Si ya has usado alguna vez Python, 
tal vez hayas oido hablar de la librería math. 
En esta librería también tenemos una función 
llamada pow() que es equivalente al operador **."""

"""import math #Siempre debe estar al principio del archivo
antes de cualquier otro código o definición.

print(math.pow(10, 3))  # 1000.0
"""
# Operadores Relacionales

"""Los operadores relacionales, o también llamados 
comparison operators nos permiten saber la relación 
existente entre dos variables. Se usan para saber 
si por ejemplo un número es mayor o menor que otro. 
Dado que estos operadores indican si se cumple o no
una operación, el valor que devuelven es True o False.
 Veamos un ejemplo con x=2 e y=3"""

"""
Operador    Nombre          Ejemplo

==	        Igual	        x == y = False
!=	        Distinto	    x != y = True
>	        Mayor	        x > y = False
&lt	        Menor	        x &lt y = True
>=	        Mayor o igual	x >= y = False
&lt=	    Menor o igual	x &lt y = True
"""
