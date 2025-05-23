class Persona:
    def __init__(self, ci="0000", nombre="SinNombre", apellido="SinApellido", celular="00000000", fecha_Nac="2000", sexo=""):
        self.__ci = ci
        self.__nombre = nombre
        self.__apellido = apellido
        self.__celular = celular
        self.__fecha_Nac = fecha_Nac
        self.__sexo = sexo

    def get_ci(self):
        return self.__ci
    def set_ci(self, ci):
        self.__ci = ci

    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_apellido(self):
        return self.__apellido
    def set_apellido(self, apellido):
        self.__apellido = apellido

    def get_celular(self):
        return self.__celular
    def set_celular(self, celular):
        self.__celular = celular

    def get_fecha_Nac(self):
        return self.__fecha_Nac
    def set_fecha_Nac(self, fecha):
        self.__fecha_Nac = fecha

    def get_sexo(self):
        return self.__sexo
    def set_sexo(self, sexo):
        self.__sexo = sexo

    def mostrar(self):
        print(f"{self.__nombre} {self.__apellido} - CI: {self.__ci} - Celular: {self.__celular} - Nacido en: {self.__fecha_Nac} - Sexo: {self.__sexo}")

    def edad(self):
        return 2025 - int(self.__fecha_Nac)


class Estudiante(Persona):
    def __init__(self, ci="0000", nombre="Estudiante", apellido="SinApellido", celular="00000000", fecha_Nac="2000", sexo="", ru="0", fecha_Ingreso="2020", semestre=1):
        super().__init__(ci, nombre, apellido, celular, fecha_Nac, sexo)
        self.__ru = ru
        self.__fecha_Ingreso = fecha_Ingreso
        self.__semestre = semestre

    def get_ru(self):
        return self.__ru
    def set_ru(self, ru):
        self.__ru = ru

    def get_fecha_Ingreso(self):
        return self.__fecha_Ingreso
    def set_fecha_Ingreso(self, fecha):
        self.__fecha_Ingreso = fecha

    def get_semestre(self):
        return self.__semestre
    def set_semestre(self, semestre):
        self.__semestre = semestre

    def mostrar(self):
        super().mostrar()
        print(f"RU: {self.__ru}, Ingreso: {self.__fecha_Ingreso}, Semestre: {self.__semestre}")


class Docente(Persona):
    def __init__(self, ci="0000", nombre="Docente", apellido="SinApellido", celular="00000000", fecha_Nac="1980", sexo="", nit="000", profesion="SinProfesion", especialidad="Ninguna"):
        super().__init__(ci, nombre, apellido, celular, fecha_Nac, sexo)
        self.__nit = nit
        self.__profesion = profesion
        self.__especialidad = especialidad

    def get_nit(self):
        return self.__nit
    def set_nit(self, nit):
        self.__nit = nit

    def get_profesion(self):
        return self.__profesion
    def set_profesion(self, profesion):
        self.__profesion = profesion

    def get_especialidad(self):
        return self.__especialidad
    def set_especialidad(self, especialidad):
        self.__especialidad = especialidad

    def mostrar(self):
        super().mostrar()
        print(f"NIT: {self.__nit}, Profesión: {self.__profesion}, Especialidad: {self.__especialidad}")

estudiantes = [
    Estudiante("123", "María", "Gómez", "7771234", "1995", "F", "RU001", "2015", 9),
    Estudiante("124", "Luis", "Pérez", "7774567", "2003", "M", "RU002", "2021", 4),
]

docentes = [
    Docente("789", "Carlos", "Gómez", "71234567", "1975", "M", "NIT001", "Ingeniero", "Sistemas"),
    Docente("790", "Lucía", "Pérez", "79876543", "1985", "F", "NIT002", "Licenciada", "Matemáticas"),
]

print("\n--- Estudiantes mayores de 25 años ---")
for est in estudiantes:
    if est.edad() > 25:
        est.mostrar()
print("\n--- Docente ingeniero, masculino y mayor ---")
mayor_docente = None
for doc in docentes:
    if doc.get_profesion().lower() == "ingeniero" and doc.get_sexo().upper() == "M":
        if mayor_docente is None or doc.edad() > mayor_docente.edad():
            mayor_docente = doc

if mayor_docente:
    mayor_docente.mostrar()
print("\n--- Coincidencia de apellidos entre estudiantes y docentes ---")
for est in estudiantes:
    for doc in docentes:
        if est.get_apellido().lower() == doc.get_apellido().lower():
            print(f"\nCoincidencia en apellido: {est.get_apellido()}")
            print("Estudiante:")
            est.mostrar()
            print("Docente:")
            doc.mostrar()
