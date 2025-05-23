
class Habitacion:
    def __init__(self, nombre, tamaño):
        self.nombre = nombre
        self.tamaño = tamaño

    def mostrar_info(self):
        print(f"Habitación: {self.nombre}, Tamaño: {self.tamaño} m²")

class Casa:
    def __init__(self, direccion):
        self.direccion = direccion
        self.habitaciones = []

    def agregar_habitacion(self, nombre, tamaño):
        habitacion = Habitacion(nombre, tamaño)
        self.habitaciones.append(habitacion)

    def mostrar_casa(self):
        print(f"Dirección: {self.direccion}")
        print("Habitaciones:")
        for habitacion in self.habitaciones:
            habitacion.mostrar_info()

casa1 = Casa("Av. del Padro")
casa1.agregar_habitacion("Sala", 20)
casa1.agregar_habitacion("Cocina", 12)
casa1.agregar_habitacion("Dormitorio", 15)

casa1.mostrar_casa()
