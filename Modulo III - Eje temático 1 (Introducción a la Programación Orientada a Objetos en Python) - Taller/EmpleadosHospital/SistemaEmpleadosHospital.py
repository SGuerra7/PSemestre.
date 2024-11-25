class EmpleadoHospital:
    def __init__(self, nombre, id, departamento, salario_base):
        self.nombre = nombre
        self.id = id
        self.departamento = departamento
        self.salario_base = salario_base

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, ID: {self.id}, Departamento: {self.departamento}, Salario Base: {self.salario_base}")

class Medico(EmpleadoHospital):
    def __init__(self, nombre, id, departamento, salario_base, especialidad, num_pacientes):
        super().__init__(nombre, id, departamento, salario_base)
        self.especialidad = especialidad
        self.num_pacientes = num_pacientes

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Especialidad: {self.especialidad}, Número de Pacientes: {self.num_pacientes}")

class Enfermero(EmpleadoHospital):
    def __init__(self, nombre, id, departamento, salario_base, turno, planta):
        super().__init__(nombre, id, departamento, salario_base)
        self.turno = turno
        self.planta = planta

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Turno: {self.turno}, Planta: {self.planta}")

medico1 = Medico("Dr. House", "M001", "Diagnóstico", 5000, "Medicina Interna", 15)
medico2 = Medico("Dr. Strange", "M002", "Traumatología", 6000, "Neurocirugía", 10)
medico3 = Medico("Dra. Grey", "M003", "Cirugía General", 5500, "Cirugía", 20)

enfermero1 = Enfermero("John Doe", "E001", "Urgencias", 3000, "Noche", 2)
enfermero2 = Enfermero("Jane Smith", "E002", "Pediatría", 3200, "Mañana", 3)
enfermero3 = Enfermero("Alice Brown", "E003", "Cardiología", 3100, "Noche", 5)

medico1.mostrar_info()
medico2.mostrar_info()
medico3.mostrar_info()

enfermero1.mostrar_info()
enfermero2.mostrar_info()
