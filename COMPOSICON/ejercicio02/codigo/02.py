
class Parte:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso

    def mostrar_info(self):
        print(f"Parte: {self.nombre}, Peso: {self.peso} kg")


    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def get_peso(self):
        return self.peso

    def set_peso(self, nuevo_peso):
        self.peso = nuevo_peso
class Avion:
    def __init__(self, modelo, fabricante):
        self.modelo = modelo
        self.fabricante = fabricante
        self.partes = []

    def agregar_parte(self, nombre, peso):
        parte = Parte(nombre, peso) 
        self.partes.append(parte)

    def mostrar_avion(self):
        print(f"Modelo: {self.modelo}")
        print(f"Fabricante: {self.fabricante}")
        print("Partes del avión:")
        for parte in self.partes:
            parte.mostrar_info()


    def get_modelo(self):
        return self.modelo

    def set_modelo(self, nuevo_modelo):
        self.modelo = nuevo_modelo

    def get_fabricante(self):
        return self.fabricante

    def set_fabricante(self, nuevo_fabricante):
        self.fabricante = nuevo_fabricante
avion1 = Avion("Boeing 747", "Boeing")

avion1.agregar_parte("Motor", 3000)
avion1.agregar_parte("Alas", 8000)
avion1.agregar_parte("Tren de aterrizaje", 1500)

avion1.mostrar_avion()
