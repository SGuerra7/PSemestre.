
def desplegar_menu():
    print("\n---Menú Opciones---\n")
    print("1. Añadir producto.")
    print("2. Actualizar producto.")
    print("3. Eliminar producto.")
    print("4. Mostrar Inventario.")
    print("5. Salir.")
    return input("\nSeleccione una opción: ")

def info_producto(is_update=False):
    nombre = input("Nombre del producto: ")

    if not is_update:
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: "))
        return nombre, cantidad, precio

    actualizar_cantidad = input("Desea actualizar cantidad? (s/n): ").lower() == 's'
    actualizar_precio = input("Desea actualizar el precio? (s/n): ").lower() == 's'

    cantidad = int(input(" Nueva Cantidad: ")) if actualizar_cantidad else None
    precio = float(input(" Nuevo precio: ")) if actualizar_precio else None

    return nombre, cantidad, precio

