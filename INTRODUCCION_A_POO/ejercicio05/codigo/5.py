class Computadora:
    def __init__(self, procesador, ram):
        self.procesador = procesador
        self.ram = ram
        self.encendida = False

    def encender(self):
        self.encendida = True

    def apagar(self):
        self.encendida = False

    def mostrar_info(self):
        print(f"Procesador: {self.procesador}")
        print(f"Memoria RAM: {self.ram}")
        estado = "encendida" if self.encendida else "apagada"
        print(f"Estado: {estado}")

mi_pc = Computadora("Intel i7", "16GB")
print("Información inicial:")
mi_pc.mostrar_info()
print("\nDespués de encender:")
mi_pc.encender()
mi_pc.mostrar_info()
print("\nDespués de apagar:")
mi_pc.apagar()
mi_pc.mostrar_info()