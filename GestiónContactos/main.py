from src.gestor_archivos import cargar_contacto
from src.gestor_contactos import agregar_contacto, actualizar_contacto, eliminar_contacto, ver_contacto
from src.menu import ver_menu, info_contacto


def main():
    lista_contactos = cargar_contacto()

    while True:
        opcion = ver_menu()

        if opcion == '1':
            nombre, telefono, correo = info_contacto()
            agregar_contacto(lista_contactos, nombre, telefono, correo)

        elif opcion == '2':
            (nombre, nuevo_nombre, telefono, correo) = info_contacto(is_update=True)
            actualizar_contacto(lista_contactos, nombre, nuevo_nombre, telefono, correo)

        elif opcion == '3':
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            eliminar_contacto(lista_contactos, nombre)

        elif opcion == '4':
            ver_contacto(lista_contactos)

        elif opcion == '5':
            print("Gracias por usar el script ;)")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
# Press the green button in the gutter to ru