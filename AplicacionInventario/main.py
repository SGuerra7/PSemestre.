from src.gestor_archivo import cargar_inventario
from src.gestor_inventario import agregar_producto, actualizar_producto, eliminar_producto, mostrar_inventario
from src.menu import desplegar_menu, info_producto


def main():
    inventario = cargar_inventario()

    while True:
        opcion = desplegar_menu()

        if opcion == '1':
            nombre, cantidad, precio = info_producto()
            agregar_producto(inventario, nombre, cantidad, precio)

        elif opcion == '2':
            nombre, cantidad, precio = info_producto(is_update=True)
            actualizar_producto(inventario, nombre, cantidad, precio)

        elif opcion == '3':
            nombre = input("Ingrese el nombre el producto a eliminar: ")
            eliminar_producto(inventario, nombre)

        elif opcion == '4':
            mostrar_inventario(inventario)

        elif opcion == '5':
            print("Gracias por usar el script ;)")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()