class Perro:
    def __init__(self,nombre,edad,raza):
        self.__nombre=nombre
        self.__edad=edad
        self.__raza=raza
    def __str__(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}, Raza: {self.__raza}"
    def hacer_sonido(self):
        print( f"el {self.__nombre}Guau")
    def moverse(self):
        print("El perro corre")
class Gato:
    def __init__(self,nombre,color):
        self.__nombre=nombre
        self.__color=color
    def __str__(self):
        return f"Nombre: {self.__nombre}, Color: {self.__color}"
    def hacer_sonido(self):
        print(f"el gato Miau")
    def moverse(self):
        print( "El gato salta")
class Pajaro:
    def __init__(self,nombre,tipo):
        self.__nombre=nombre
        self.__tipo=tipo
    def __str__(self):
        return f"Nombre: {self.__nombre}, Tipo: {self.__tipo}"
    def hacer_sonido(self):
        print( "Pío")
    def moverse(self):
        print( "El pájaro vuela")
perro=Perro("Firulais", 5, "Labrador")
gato=Gato("gorda", "Blanco")
pajaro=Pajaro("pajaro  loca", "Canario")
print(perro)
perro.hacer_sonido()
perro.moverse()
print(gato)
gato.hacer_sonido()
gato.moverse()
print(pajaro)
pajaro.hacer_sonido()
pajaro.moverse()