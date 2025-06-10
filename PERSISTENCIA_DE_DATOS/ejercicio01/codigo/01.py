
class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def __str__(self):
        return f"{self.nombre},{self.edad},{self.salario}"

    @staticmethod
    def desde_texto(linea):
        nombre, edad, salario = linea.strip().split(',')
        return Empleado(nombre, int(edad), float(salario))

class ArchivoEmpleado:
    def __init__(self, nomA):
        self.nomA = nomA

    def crearArchivo(self):
        with open(self.nomA, 'w') as archivo:
            pass 
        print("Archivo creado correctamente.")

    def guardarEmpleado(self, empleado):
        with open(self.nomA, 'a') as archivo:
            archivo.write(str(empleado) + '\n')
        print(f"Empleado {empleado.nombre} guardado con éxito.")

    def cargarEmpleados(self):
        empleados = []
        try:
            with open(self.nomA, 'r') as archivo:
                for linea in archivo:
                    empleados.append(Empleado.desde_texto(linea))
        except FileNotFoundError:
            print("El archivo no existe.")
        return empleados

    def buscaEmpleado(self, nombre):
        empleados = self.cargarEmpleados()
        for emp in empleados:
            if emp.nombre == nombre:
                return emp
        return None

    def mayorSalario(self, sueldo):
        empleados = self.cargarEmpleados()
        for emp in empleados:
            if emp.salario > sueldo:
                return emp
        return None
archivo = ArchivoEmpleado("empleados.txt")
archivo.crearArchivo()
archivo.guardarEmpleado(Empleado("Ana", 30, 2500))
archivo.guardarEmpleado(Empleado("Luis", 28, 3200))
archivo.guardarEmpleado(Empleado("Carlos", 40, 1500))
empleado = archivo.buscaEmpleado("Luis")
if empleado:
    print("Empleado encontrado:", empleado.nombre, empleado.edad, empleado.salario)
else:
    print("Empleado no encontrado.")
empleadoMayor = archivo.mayorSalario(2000)
if empleadoMayor:
    print("Empleado con mayor salario:", empleadoMayor.nombre, empleadoMayor.salario)
else:
    print("Ninguno tiene salario mayor.")

