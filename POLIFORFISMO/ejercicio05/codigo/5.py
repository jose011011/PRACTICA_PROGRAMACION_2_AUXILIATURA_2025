class BloqueCofre:
    def __init__(self, capacidad, resistencia, tipo="Cofre"):
        self.tipo = tipo
        self.capacidad = capacidad
        self.resistencia = resistencia

    def accion(self):
        print(f"Abriendo cofre. Almacena {self.capacidad} items.")

    def romper(self):
        print(f"¡Cofre roto! Soltó {self.capacidad} objetos.")

    def colocar(self, orientacion="suelo"):
        print(f"Cofre colocado en {orientacion}.")

class BloqueTnt:
    def __init__(self, daño, tipo="TNT"):
        self.tipo = tipo
        self.daño = daño
        self.resistencia = 5

    def accion(self):
        print(f"¡TNT activada! Causará {self.daño} de daño.")

    def romper(self):
        print(f"¡BOOM! Explosión de {self.daño} puntos.")

    def colocar(self, orientacion="suelo"):
        print(f"TNT colocada en {orientacion}.")

class BloqueHorno:
    def __init__(self, color, capacidad_comida, tipo="Horno"):
        self.tipo = tipo
        self.color = color
        self.capacidad_comida = capacidad_comida
        self.resistencia = 10 

    def accion(self):
        print(f"Horno {self.color} hornea {self.capacidad_comida} unidades.")

    def romper(self):
        print(f"Horno {self.color} roto. Liberó {self.capacidad_comida} alimentos.")

    def colocar(self, orientacion="suelo"):
        print(f"Horno colocado en {orientacion}.")


cofre1 = BloqueCofre(100, 50)
cofre2 = BloqueCofre(200, 75)
tnt1 = BloqueTnt(20)
tnt2 = BloqueTnt(30)
horno1 = BloqueHorno("Rojo", 10)
horno2 = BloqueHorno("Gris", 20)


bloques = [cofre1, cofre2, tnt1, tnt2, horno1, horno2]

print("=== Acciones ===")
for bloque in bloques:
    bloque.accion()  


print("\n=== Colocar bloques ===")
cofre1.colocar()
tnt1.colocar("pared")
horno1.colocar("techo")


print("\n=== Romper bloques ===")
for bloque in bloques:
    bloque.romper()