
from .gestor_archivo import guardar_inventario


def agregar_producto(inventario, nombre, cantidad, precio):

    if nombre in inventario:
        print("El producto ya existe.")
        return False
    inventario[nombre] = {
        "Cantidad": cantidad,
        "Precio": float(precio)
    }

    return guardar_inventario(inventario)

def actualizar_producto(inventario, nombre, cantidad=0, precio=0):
        if nombre not in inventario:
            print("El producto no se encuentra en el inventario.")
            return False

        if cantidad is not None:
            inventario[nombre]['Cantidad'] = int(cantidad)
        if precio is not None:
            inventario[nombre]['Precio'] = float(precio)

        return guardar_inventario(inventario)


def eliminar_producto(inventario, nombre):
        if nombre not in inventario:
            print("El producto no se encuentra en el inventario.")
            return False

        del inventario[nombre]

        return guardar_inventario(inventario)


def mostrar_inventario(inventario):
    print(f" Tipo de inventario: {type(inventario)}")
    print(f" Contenido de inventario: {inventario}")


    if not inventario:
        print("\nEl inventario está vacío.")
        return
    print("Inventario Actual:")
    print("-" * 50)
    print(f"{'Producto':<20} {'Cantidad':<12} {'Precio':<10}")
    print("-" * 50)

    try:
        if not isinstance(inventario, dict):
            print("Error: El invenetario  no es un diccionario válido.")
            return


        for nombre, datos in inventario.items():
            print(f"{nombre:<21}{datos['Cantidad']:<12} ${datos['Precio']:<10.2f}")
    except Exception as e:
        print(f" Error al mostrar el inventario: {e}")
    print("-" * 50)

    return

