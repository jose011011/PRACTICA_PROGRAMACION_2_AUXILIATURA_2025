class Empleado:
    def __init__(self, nombre, apellido, salario_base, anios_antiguedad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__salario_base = salario_base
        self.__anios_antiguedad = anios_antiguedad
    def get_nombre(self):
        return self.__nombre
    def get_apellido(self):
        return self.__apellido
    def get_salario_base(self):
        return self.__salario_base
    def get_anios_antiguedad(self):
        return self.__anios_antiguedad
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_apellido(self, apellido):
        self.__apellido = apellido
    def set_salario_base(self, salario):
        self.__salario_base = salario
    def set_anios_antiguedad(self, anios):
        self.__anios_antiguedad = anios
    def calcular_salario(self):
        bono = self.__salario_base * 0.05 * self.__anios_antiguedad
        return self.__salario_base + bono
class Gerente(Empleado):
    def __init__(self, nombre, apellido, salario_base, anios_antiguedad, departamento, bono_gerencial):
        super().__init__(nombre, apellido, salario_base, anios_antiguedad)
        self.__departamento = departamento
        self.__bono_gerencial = bono_gerencial
    def get_departamento(self):
        return self.__departamento
    def get_bono_gerencial(self):
        return self.__bono_gerencial
    def set_departamento(self, departamento):
        self.__departamento = departamento
    def set_bono_gerencial(self, bono):
        self.__bono_gerencial = bono
    def calcular_salario(self):
        salario_base_con_bonos = super().calcular_salario()
        return salario_base_con_bonos + self.__bono_gerencial
class Desarrollador(Empleado):
    def __init__(self, nombre, apellido, salario_base, anios_antiguedad, lenguaje_programacion, horas_extras):
        super().__init__(nombre, apellido, salario_base, anios_antiguedad)
        self.__lenguaje_programacion = lenguaje_programacion
        self.__horas_extras = horas_extras
    def get_lenguaje_programacion(self):
        return self.__lenguaje_programacion
    def get_horas_extras(self):
        return self.__horas_extras
    def set_lenguaje_programacion(self, lenguaje):
        self.__lenguaje_programacion = lenguaje
    def set_horas_extras(self, horas):
        self.__horas_extras = horas
    def calcular_salario(self):
        salario_base_con_bonos = super().calcular_salario()
        extra = self.__horas_extras * 20  
        return salario_base_con_bonos + extra
g1 = Gerente("Laura", "Gómez", 3000, 10, "Finanzas", 1200)
g2 = Gerente("Carlos", "Pérez", 2800, 7, "Marketing", 800)
d1 = Desarrollador("Ana", "López", 2000, 5, "Python", 12)
d2 = Desarrollador("Juan", "Martínez", 2200, 3, "Java", 8)

empleados = [g1, g2, d1, d2]

print("=== Salarios Calculados ===")
for e in empleados:
    print(f"{e.get_nombre()} {e.get_apellido()} - {type(e).__name__}: {e.calcular_salario()} €")
print("\n=== Gerentes con bono gerencial > 1000 ===")
for e in empleados:
    if isinstance(e, Gerente) and e.get_bono_gerencial() > 1000:
        print(f"{e.get_nombre()} {e.get_apellido()}, Bono: {e.get_bono_gerencial()} €")

print("\n=== Desarrolladores con más de 10 horas extras ===")
for e in empleados:
    if isinstance(e, Desarrollador) and e.get_horas_extras() > 10:
        print(f"{e.get_nombre()} {e.get_apellido()}, Horas Extras: {e.get_horas_extras()}")
