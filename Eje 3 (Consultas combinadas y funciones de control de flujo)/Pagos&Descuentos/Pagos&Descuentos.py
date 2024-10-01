from colorama import Fore, Style, init
init()

articulos = []
def ingresar_articulos():
    descuento = 0
    subtotal = 0
    antes_desc = 0
    desp_desc = 0

    while True:
        nombre = input("Ingrese el nombre del articulo (Digíte 0 para finalizar): ")

        if nombre == '0':
            print(Fore.MAGENTA + " Detalles de Factura: " + Style.RESET_ALL)

            print( f" Número de articulos totales: {Fore.MAGENTA}{len(articulos)}{Style.RESET_ALL} ")
            for articulo in articulos:
                print(f"    Articulo: {Fore.LIGHTBLUE_EX}{articulo['nombre']}{Style.RESET_ALL}"
                      f", Precio: {Fore.LIGHTBLUE_EX}{articulo['precio']}{Style.RESET_ALL}, "
                      f"Cantidad: {Fore.LIGHTBLUE_EX}{articulo['cantidad']}{Style.RESET_ALL}, "
                      f"Total por artículo: {Fore.LIGHTBLUE_EX}{articulo['ttl_art_']}{Style.RESET_ALL}")

            if descuento > 0:
                print(f" Total antes del descuento: {Fore.YELLOW}{antes_desc}{Style.RESET_ALL}")
                print(f" Total después del descuento: {Fore.LIGHTCYAN_EX}{desp_desc}{Style.RESET_ALL}" )
            print(f"    Subtotal: {Fore.LIGHTGREEN_EX}{subtotal}{Style.RESET_ALL}")
            if len(articulos) >= 3:
                print(f' Método de pago recomendado: {Fore.GREEN}Targeta{Style.RESET_ALL}')
                cargo_adicional = 0.02 * subtotal
                print(f" Cargo adicional por medio de pago con targeta: "
                      f"{Fore.LIGHTBLUE_EX}{cargo_adicional}{Style.RESET_ALL}")
                print(f' Total a pagar: {Fore.LIGHTGREEN_EX}{cargo_adicional + subtotal}{Style.RESET_ALL} ')
            elif len(articulos) < 3:
                print(f" Método de pago recomendado: {Fore.GREEN}Efectivo{Style.RESET_ALL}")
                print(f" Total a pagar: {Fore.LIGHTGREEN_EX}{subtotal}{Style.RESET_ALL}")

            return articulos

        try:
            precio = float(input(" Ingrese el precio del articulo: "))
            cantidad = int(input("  Ingrese la cantidad de articulos: "))
        except ValueError:
            print(Fore.RED + "Error: Digíte números válidos." + Style.RESET_ALL)
            continue

        articulo = {
            'nombre' : nombre,
            'precio' : precio,
            'cantidad' : cantidad,
            'ttl_art_' : precio * cantidad
        }
        """print(f"\nDEBUG: Artículo ingresado: {articulo}")"""

        articulos.append(articulo)

        total_art = precio * cantidad
        antes_desc += total_art

        if len(articulos) >= 5:
            descuento = 0.20 * antes_desc

        elif 3 <= len(articulos) <= 4:
            descuento = 0.10 * antes_desc
        else:
            descuento = 0

        total_con_descuento = total_art - descuento
        desp_desc = antes_desc - descuento

        print(f"Articulo registrado: {Fore.LIGHTBLUE_EX}{articulo['nombre']}{Style.RESET_ALL}, "
              f"Precio: {Fore.LIGHTBLUE_EX}{articulo['precio']}{Style.RESET_ALL}, "
              f"Cantidad: {Fore.LIGHTBLUE_EX}{articulo['cantidad']}{Style.RESET_ALL}")
        print(f" Total a pagar por articulo: {Fore.LIGHTBLUE_EX}{articulo['ttl_art_']}{Style.RESET_ALL}")
        if descuento > 0:

            print(f" Descuento aplicado: {Fore.LIGHTGREEN_EX}{descuento}{Style.RESET_ALL}")
            print(f" Total con descuento: {Fore.LIGHTGREEN_EX}{total_con_descuento}{Style.RESET_ALL}")

        subtotal = desp_desc
        print(f"Subtotal actual: {Fore.LIGHTCYAN_EX}{subtotal}{Style.RESET_ALL}")

    return articulos

ingresar_articulos()