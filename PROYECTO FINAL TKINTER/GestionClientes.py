from random import uniform

import mysql.connector
from tkinter import Tk, ttk, messagebox, StringVar, Entry, Text, Scrollbar, VERTICAL, END
from tabulate import tabulate

class DatabaseConnector:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Conexión exitosa a la base de datos.")
        except mysql.connector.Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def execute_procedure(self, procedure_name, params):
        try:
            cursor = self.connection.cursor()
            cursor.callproc(procedure_name, params)
            self.connection.commit()
            cursor.close()
        except mysql.connector.Error as e:
            print(f"Error ejecutando el procedimiento {procedure_name}: {e}")

    def fetch_procedure_results(self, procedure_name, params):
        try:
            cursor = self.connection.cursor()
            cursor.callproc(procedure_name, params)
            results = []
            for result in cursor.stored_results():
                results.extend(result.fetchall())
            cursor.close()
            return results
        except mysql.connector.Error as e:
            print(f"Error obteniendo resultados del procedimiento {procedure_name}: {e}")
            return []

    def close(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Conexión cerrada.")

class Application:
    def __init__(self, root, db_connector):
        self.root = root
        self.db = db_connector

        self.root.title("Gestión de Clientes")
        self.root.geometry("930x600")

        self.result_area = None
        self.create_widgets()

    def create_widgets(self):
        # Crear variables para los campos
        self.nombre_var = StringVar()
        self.email_var = StringVar()
        self.telefono_var = StringVar()
        self.direccion_var = StringVar()
        self.categoria_var = StringVar()
        self.valor_var = StringVar()
        self.cliente_id_var = StringVar()

        # Frame principal
        frame = ttk.Frame(self.root)
        self.root.resizable(False, False)
        frame.pack(padx=10, pady=10, fill='both', expand=True)

        # Configurar columnas uniformemente
        for i in range(6):
            frame.columnconfigure(i, weight=1, uniform="col")
        for j in range(5):
            frame.rowconfigure(j, weight=1, uniform="row")  # uniform asegura igual espacio

        # Ancho fijo para los campos de entrada
        entry_width = 20

        # Fila 0
        ttk.Label(frame, text="Nombre:").grid(row=0, column=0, padx=2, pady=2, sticky='e')
        Entry(frame, textvariable=self.nombre_var, width=entry_width).grid(row=0, column=1, padx=2, pady=2, sticky='ew')

        ttk.Label(frame, text="Email:").grid(row=0, column=2, padx=2, pady=2, sticky='e')
        Entry(frame, textvariable=self.email_var, width=entry_width).grid(row=0, column=3, padx=2, pady=2, sticky='ew')

        ttk.Label(frame, text="Cliente ID:").grid(row=0, column=4, padx=2, pady=2, sticky='e')
        Entry(frame, textvariable=self.cliente_id_var, width=entry_width).grid(row=0, column=5, padx=2, pady=2,
                                                                               sticky='ew')

        # Fila 1
        ttk.Label(frame, text="Teléfono:").grid(row=1, column=0, padx=2, pady=2, sticky='e')
        Entry(frame, textvariable=self.telefono_var, width=entry_width).grid(row=1, column=1, padx=2, pady=2,
                                                                             sticky='ew')

        ttk.Label(frame, text="Dirección:").grid(row=1, column=2, padx=2, pady=2, sticky='e')
        Entry(frame, textvariable=self.direccion_var, width=entry_width).grid(row=1, column=3, padx=2, pady=2,
                                                                              sticky='ew')

        # Fila 2
        ttk.Label(frame, text="Categoría:").grid(row=2, column=0, padx=2, pady=2, sticky='e')
        Entry(frame, textvariable=self.categoria_var, width=entry_width).grid(row=2, column=1, padx=2, pady=2,
                                                                              sticky='ew')

        ttk.Label(frame, text="Valor:").grid(row=2, column=2, padx=2, pady=2, sticky='e')
        Entry(frame, textvariable=self.valor_var, width=entry_width).grid(row=2, column=3, padx=2, pady=2, sticky='ew')

        # Botones
        ttk.Button(frame, text="Registrar Cliente", command=self.register_client).grid(row=3, column=1, pady=10)
        ttk.Button(frame, text="Actualizar Cliente", command=self.update_client).grid(row=3, column=2, pady=10)
        ttk.Button(frame, text="Eliminar Cliente", command=self.delete_client).grid(row=3, column=3, pady=10)
        ttk.Button(frame, text="Buscar Cliente", command=self.search_client).grid(row=4, column=1, pady=10)
        ttk.Button(frame, text="Generar Informe", command=self.generate_report).grid(row=4, column=2, pady=10)
        ttk.Button(frame, text="Estadísticas de Fidelidad", command=self.calculate_loyalty).grid(row=4, column=3,
                                                                                                 pady=10)

        # Área de resultados
        self.result_area = Text(self.root, wrap='word', height=25, width=100)
        self.result_area.pack(pady=10, padx=10, fill='both')

        scrollbar = Scrollbar(self.root, command=self.result_area.yview, orient=VERTICAL)
        self.result_area.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side='right', fill='y')

    def clear_fields(self):
        self.nombre_var.set("")
        self.email_var.set("")
        self.telefono_var.set("")
        self.direccion_var.set("")
        self.categoria_var.set("")
        self.valor_var.set("")
        self.cliente_id_var.set("")

    def display_results(self, results, headers):
        self.result_area.delete(1.0, END)
        if results:
            table = tabulate(results, headers=headers, tablefmt="grid")
            self.result_area.insert(END, table)
        else:
            self.result_area.insert(END, "No se encontraron resultados.")

    def register_client(self):
        try:
            nombre = self.nombre_var.get()
            email = self.email_var.get()
            telefono = self.telefono_var.get()
            direccion = self.direccion_var.get()

            self.db.execute_procedure("RegistrarCliente", (nombre, email, telefono, direccion))
            messagebox.showinfo("Éxito", "Cliente registrado exitosamente.")
            self.clear_fields()
        except Exception as e:
            messagebox.showerror("Error", f"Error registrando cliente: {e}")

    def update_client(self):
        try:
            cliente_id = int(self.cliente_id_var.get())
            email = self.email_var.get()
            telefono = self.telefono_var.get()
            direccion = self.direccion_var.get()
            categoria = self.categoria_var.get()
            valor = self.valor_var.get()

            self.db.execute_procedure(
                "ActualizarPreferenciasYContacto", (cliente_id, email, telefono, direccion, categoria, valor)
            )
            messagebox.showinfo("Éxito", "Datos del cliente actualizados correctamente.")
            self.clear_fields()
        except Exception as e:
            messagebox.showerror("Error", f"Error actualizando cliente: {e}")

    def delete_client(self):
        try:
            cliente_id = int(self.cliente_id_var.get())

            self.db.execute_procedure("EliminarCliente", (cliente_id,))
            messagebox.showinfo("Éxito", "Cliente eliminado correctamente.")
            self.clear_fields()
        except Exception as e:
            messagebox.showerror("Error", f"Error eliminando cliente: {e}")

    def search_client(self):
        try:
            cliente_id = int(self.cliente_id_var.get())
            results = self.db.fetch_procedure_results("BuscarCliente", (cliente_id,))

            if results:
                headers = ["ID", "Nombre", "Email", "Teléfono", "Dirección", "Categoría", "Valor"]
                self.display_results(results, headers)
            else:
                messagebox.showinfo("Búsqueda", "Cliente no encontrado.")
        except Exception as e:
            messagebox.showerror("Error", f"Error buscando cliente: {e}")

    def generate_report(self):
        try:
            results = self.db.fetch_procedure_results("GenerarInformeVentas", ())
            headers = ["ID", "Nombre", "Total Compras", "Última Compra"]
            self.display_results(results, headers)
        except Exception as e:
            messagebox.showerror("Error", f"Error generando informe: {e}")

    def calculate_loyalty(self):
        try:
            results = self.db.fetch_procedure_results("CalcularEstadisticasFidelidad", ())
            headers = ["ID", "Nombre", "Puntos de Fidelidad", "Nivel"]
            self.display_results(results, headers)
        except Exception as e:
            messagebox.showerror("Error", f"Error calculando estadísticas de fidelidad: {e}")

if __name__ == "__main__":
    db_connector = DatabaseConnector(host="localhost", user="root", password="", database="EmpresaSoftware")
    db_connector.connect()

    root = Tk()
    app = Application(root, db_connector)
    root.mainloop()

    db_connector.close()
