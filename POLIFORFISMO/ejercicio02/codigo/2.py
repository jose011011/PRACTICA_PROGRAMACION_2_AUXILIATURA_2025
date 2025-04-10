class Cocinero:
    def __init__(self,nombre,sueldoMes,horasExtras,sueldohora):
        self.__nombre=nombre
        self.__sueldoMes=sueldoMes
        self.__horasEx=horasExtras
        self.__sueldoHo=sueldohora
    def __str__(self):
        return f"Nombre: {self.__nombre}, Sueldo mensual: {self.__sueldoMes}, Horas extras: {self.__horasEx}, Sueldo por hora: {self.__sueldoHo}"

    def SueldoTotal(self):
        s=self.__sueldoMes+(self.__horasEx*self.__sueldoHo)
        return s
    def get_sueldoMes(self):
        return self.__sueldoMes
        

class Mesero:
    def __init__(self,nombre,sueldomes,horasextras,sueldohora,propina):
        self.__nombre=nombre
        self.__sueldoMes=sueldomes
        self.__horasEx=horasextras
        self.__sueldoHo=sueldohora
        self.__propina=propina
    def __str__(self):
        return f"Nombre: {self.__nombre}, Sueldo mensual: {self.__sueldoMes}, Horas extras: {self.__horasEx}, Sueldo por hora: {self.__sueldoHo}"

    def SueldoTotal(self):
        s=self.__sueldoMes+(self.__horasEx*self.__sueldoHo)+self.__propina
        return s
    def get_sueldoMes(self):
        return self.__sueldoMes
class Administrativo:
    def __init__(self,nombre,sueldomes,cargo):
        self.__nombre=nombre
        self.__sueldoMes=sueldomes
        self.__cargo=cargo
    def __str__(self):
        return f"Nombre: {self.__nombre}, Sueldo mensual: {self.__sueldoMes}, Cargo: {self.__cargo}"
    def SueldoTotal(self):
        return self.__sueldoMes
    def get_sueldoMes(self):
        return self.__sueldoMes
    
def buscar_sueldo(empleados, sueldoX):
    print(f"Empleados con sueldo mensual igual a {sueldoX}:")
    for empleado in empleados:
        if empleado.get_sueldoMes() == sueldoX:
            print(empleado)

def mostrar_sueldos_totales(empleados):
    print("Sueldos totales de los empleados:")
    for empleado in empleados:
        print(f"{empleado}: Sueldo Total: {empleado.SueldoTotal()}")
    
cocinero1 = Cocinero("Carlos", 15000, 10, 200)
mesero1 = Mesero("Juan", 10000, 5, 150, 500)
mesero2 = Mesero("Luis", 10500, 8, 150, 700)
admin1 = Administrativo("Ana", 18000, "Gerente")
admin2 = Administrativo("Pedro", 16000, "Supervisor")
print(cocinero1)
print(mesero1)
print(mesero2)
print(admin1)
print(admin2)
print("Sueldo total cocinero: ", cocinero1.SueldoTotal())
print("Sueldo total mesero1: ", mesero1.SueldoTotal())
print("Sueldo total mesero2: ", mesero2.SueldoTotal())
print("Sueldo total admin1: ", admin1.SueldoTotal())
print("Sueldo total admin2: ", admin2.SueldoTotal())
print("Buscar empleados con sueldo mensual de 10000")
empleados = [cocinero1, mesero1, mesero2, admin1, admin2]
buscar_sueldo(empleados, 10000)


