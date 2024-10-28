
from .gestor_archivos import guardar_contacto


def agregar_contacto(contacto, nombre, telefono, correo):

    if nombre in contacto:
        print("El contacto ya existe.")
        return False
    contacto[nombre] = {
        "Télefono": int(telefono),
        "Correo": correo
    }
    print(f"{nombre} Se ha agregado a tu lista de contactos. ")
    return guardar_contacto(contacto)

"""    if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
        print("El formato del correo electrónico es inválido.")
        return False"""


def actualizar_contacto(contacto, nombre_original, nuevo_nombre, telefono, correo):

    if nombre_original not in contacto:
        print("El contacto no se encuentra en tu lista de contactos.")
        return False
    if nuevo_nombre:
        contacto[nuevo_nombre] = contacto.pop(nombre_original)
        nombre = nuevo_nombre
    else:
        nombre = nombre_original

    if telefono is not None:
        contacto[nombre]['Télefono'] = int(telefono)
    if correo is not None:
        contacto[nombre]['Correo'] = correo

    return guardar_contacto(contacto)

def eliminar_contacto(contacto, nombre):
        if nombre not in contacto:
            print("El contacto no se encuentra registrado.")
            return False
        else:
            print(f" {contacto} Ha sido eliminado de tu lista de contactos.")

        del contacto[nombre]

        return guardar_contacto(contacto)


def ver_contacto(contactos):

    if not contactos:
        print("\n Lista de contactos está vacía.")
        return
    print("Lista de contactos:")
    print("-" * 50)
    print(f"{'Contacto':<20} {'Télefono':<12} {'Correo':<10}")
    print("-" * 50)

    try:
        if not isinstance(contactos, dict):
            print("Error: La lista de contactos no es válida.")
            return
        for nombre, datos in contactos.items():
            print(f"{nombre:<21}{datos['Télefono']:<15} ${datos['Correo']:<24}")
    except Exception as e:
        print(f" Error al mostrar lista de contactos: {e}")
    print("-" * 50)

    return

