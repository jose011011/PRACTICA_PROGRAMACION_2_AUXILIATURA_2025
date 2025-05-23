
class Estudiante:
    def __init__(self, nombre, carrera, semestre):
        self.nombre = nombre
        self.carrera = carrera
        self.semestre = semestre

    def mostrar_info(self):
        print(f"Estudiante: {self.nombre}, Carrera: {self.carrera}, Semestre: {self.semestre}")


    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def get_carrera(self):
        return self.carrera

    def set_carrera(self, nueva_carrera):
        self.carrera = nueva_carrera

    def get_semestre(self):
        return self.semestre

    def set_semestre(self, nuevo_semestre):
        self.semestre = nuevo_semestre
class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def mostrar_universidad(self):
        print(f"Universidad: {self.nombre}")
        print("Estudiantes:")
        for estudiante in self.estudiantes:
            estudiante.mostrar_info()


    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
est1 = Estudiante("Laura", "Ingeniería", 3)
est2 = Estudiante("Mario", "Medicina", 5)
est3 = Estudiante("Sofía", "Derecho", 2)

uni = Universidad("Universidad Central")
uni.agregar_estudiante(est1)
uni.agregar_estudiante(est2)
uni.agregar_estudiante(est3)

uni.mostrar_universidad()
