class Videojuego:
    def __init__(self,nombre,platafroma,cant_jugado=0):
        self.__nombre=nombre
        self.__platafroma=platafroma
        self.__cant_jugador=cant_jugado
        
    def agregar_jugadores(self,n=1):
        self.__cant_jugador=self.__cant_jugador+n
        print("se agrego correctamente")
        print(f"los jugadores actuales son: {self.__cant_jugador}")
        
    def mostrar(self):
        print(f"nombre del juego: {self.__nombre} \nplataforma: {self.__platafroma} \ncamtidad de jugadores: {self.__cant_jugador}")


juego1 = Videojuego("Fortnite", "PC", 100)
juego2 = Videojuego("Minecraft", "Consola",)

print("Información inicial de juego1:")
juego1.mostrar()
print("\nInformación inicial de juego2:")
juego2.mostrar()

print("\nAgregando 5 jugadores a juego1:")
juego1.agregar_jugadores(5)
print("\nAgregando 1 jugador a juego2:")
juego2.agregar_jugadores()

print("\nInformación actualizada de juego1:")
juego1.mostrar()
print("\nInformación actualizada de juego2:")
juego2.mostrar()