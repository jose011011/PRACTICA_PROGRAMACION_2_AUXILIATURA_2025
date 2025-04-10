class Oficina:
    def __init__(self,nsrSillas,nroEscritorios,nroEstanteria):
        self.__nroSillas=nsrSillas
        self.__nroEscritorios=nroEscritorios
        self.__nroEstanteria=nroEstanteria
    def __str__(self):
        return f"Numero de sillas de la oficina: {self.__nroSillas}, Numero de escritorios: {self.__nroEscritorios}, Numero de estanteria: {self.__nroEstanteria}"
    def cantidadMuebles(self):
        return self.__nroSillas+self.__nroEscritorios+self.__nroEstanteria

class Aula:
    def __init__(self,nombre,capacidad,nroPupitres):
        self.__nombre=nombre
        self.__capacidad=capacidad
        self.__nroPupitres=nroPupitres
    def __str__(self):
        return f"Nombre de la aula: {self.__nombre}, Capacidad: {self.__capacidad}, Numero de pupitres: {self.__nroPupitres}"
    def cantidadMuebles(self):
        return self.__nroPupitres
class Laboratorio:
    def __init__(self,nombre,capacidad,nroMsesas,nroSillas):
        self.__nombre=nombre
        self.__capacidad=capacidad
        self.__nroMesas=nroMsesas
        self.__nroSillas=nroSillas
    def __str__(self):
        return f"Nombre del laboratorio: {self.__nombre}, Capacidad: {self.__capacidad}, Numero de mesas: {self.__nroMesas}, Numero de sillas: {self.__nroSillas}"
    def cantidadMuebles(self):
        return self.__nroMesas+self.__nroSillas
    
oficia1=Oficina(10,5,2)
aficina2=Oficina(8,4,3)
aula1=Aula("A1",30,20)
aula2=Aula("A2",25,15)
lab1=Laboratorio("Lab1",20,5,10)
print(oficia1)
print("Cantidad de muebles oficina1: ",oficia1.cantidadMuebles())
print("-"*30)
print(aficina2)
print("Cantidad de muebles oficina2: ",aficina2.cantidadMuebles())
print("-"*30)
print(aula1)
print("Cantidad de muebles aula1: ",aula1.cantidadMuebles())
print("-"*30)
print(aula2)
print("Cantidad de muebles aula2: ",aula2.cantidadMuebles())
print("-"*30)
print(lab1)
print("Cantidad de muebles laboratorio1: ",lab1.cantidadMuebles())

