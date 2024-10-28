from src.gestor_contactos import ver_contacto

def ver_menu():
    print(f"\n ---Menú---  \n")
    print(f"1. Añadir Contacto")
    print(f"2. Actualizar Contactos")
    print(f"3. Eliminar un Contacto")
    print(f"4. Ver Contactos")
    print(f"5. Salir")
    return input("\nSeleccione una opción: ")

def info_contacto(is_update=False):
    nombre = input("Nombre del contacto: ")

    if not is_update:
        telefono = int(input("Télefono: "))
        correo = input("Correo: ")
        return nombre, telefono, correo

    actualizar_nombre = input("Desea actualizar el nombre? (s/n): ").lower() == 's'
    actualizar_telefono = input("Desea actualizar el Télefono? (s/n): ").lower() == 's'
    actualizar_correo = input("Desea actualizar el correo? (s/n): ").lower() == 's'
    nuevo_nombre = input(" Nuevo nombre: ") if actualizar_nombre else None
    telefono = int(input(" Nuevo télefono: ")) if actualizar_telefono else None
    correo = input(" Nuevo correo: ") if actualizar_correo else None
    print(f"Contacto: {nuevo_nombre} se ha actualizado correctamente.")
    return nombre, nuevo_nombre, telefono, correo