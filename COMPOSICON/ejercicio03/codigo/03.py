class Jugador:
    def __init__(self, nombre, numero, posicion):
        self.nombre = nombre
        self.numero = numero
        self.posicion = posicion

    def mostrar_info(self):
        print(f"Jugador: {self.nombre}, Número: {self.numero}, Posición: {self.posicion}")

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def get_numero(self):
        return self.numero

    def set_numero(self, nuevo_numero):
        self.numero = nuevo_numero

    def get_posicion(self):
        return self.posicion

    def set_posicion(self, nueva_posicion):
        self.posicion = nueva_posicion
class Portero(Jugador):
    def __init__(self, nombre, numero, habilidad_especial):
        super().__init__(nombre, numero, "Portero")
        self.habilidad_especial = habilidad_especial

    def mostrar_info(self):
        super().mostrar_info()
        print(f"  Habilidad especial: {self.habilidad_especial}")


class Defensa(Jugador):
    def __init__(self, nombre, numero, habilidad_especial):
        super().__init__(nombre, numero, "Defensa")
        self.habilidad_especial = habilidad_especial

    def mostrar_info(self):
        super().mostrar_info()
        print(f"  Habilidad especial: {self.habilidad_especial}")


class Mediocampista(Jugador):
    def __init__(self, nombre, numero, habilidad_especial):
        super().__init__(nombre, numero, "Mediocampista")
        self.habilidad_especial = habilidad_especial

    def mostrar_info(self):
        super().mostrar_info()
        print(f"  Habilidad especial: {self.habilidad_especial}")


class Delantero(Jugador):
    def __init__(self, nombre, numero, habilidad_especial):
        super().__init__(nombre, numero, "Delantero")
        self.habilidad_especial = habilidad_especial

    def mostrar_info(self):
        super().mostrar_info()
        print(f"  Habilidad especial: {self.habilidad_especial}")

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def mostrar_equipo(self):
        print(f"Equipo: {self.nombre}")
        print("Jugadores:")
        for jugador in self.jugadores:
            jugador.mostrar_info()

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
equipo1 = Equipo("Tigres FC")
equipo1.agregar_jugador(Portero("Carlos", 1, "Atajadas"))
equipo1.agregar_jugador(Defensa("Luis", 4, "Marcaje"))
equipo1.agregar_jugador(Mediocampista("Juan", 8, "Pases precisos"))
equipo1.agregar_jugador(Delantero("Pedro", 9, "Goles potentes"))

equipo1.mostrar_equipo()
