import json
from pathlib import Path


def cargar_inventario():
    file_path = Path("datos/inventario.json")

    file_path.parent.mkdir(exist_ok=True)

    try:
        if file_path.exists():
            with open(file_path, 'r') as file:
                return json.load(file)
        return {}
    except json.JSONDecodeError:
        print("Error en el archivo. Creando nuevo inventario.")
        return {}


def guardar_inventario(inventario):
    file_path = Path("datos/inventario.json")

    try:
        with open(file_path, 'w') as file:
            json.dump(inventario, file, indent=4)
            return True
    except Exception as e:
        print(f"Error al guardar: {e}")
        return False

