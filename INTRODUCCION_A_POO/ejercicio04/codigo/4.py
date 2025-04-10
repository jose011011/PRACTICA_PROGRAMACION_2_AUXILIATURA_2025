class Celular:
    def __init__(self,nombre,peso):
        self.__aplicaciones = []
        self.__espacio_total = 1024  
        self.__espacio_usado = 0  
        self.__bateria = 100  
        self.__nombre = nombre
        self.__peso = peso

    def consumo_bateria(self, tiempo):
        return tiempo * 0.1

    def instalar_aplicacion(self):

        if self.__espacio_usado + self.__peso <= self.__espacio_total:
            self.__aplicaciones.append(self.__nombre)
            self.__espacio_usado += self.__peso
            print(f"Aplicación '{self.__nombre}' instalada correctamente.")
        else:
            print("No hay suficiente espacio para instalar la aplicación.")

    def utilizar_aplicacion(self, nombre, tiempo):
        self.__nombre = next((self.__nombre for self.__nombre in self.__aplicaciones if self.__nombre == nombre), None)
        if self.__nombre:
            consumo = self.consumo_bateria(tiempo)
            self.__bateria -= consumo
            print(f"Aplicación '{nombre}' utilizada durante {tiempo} minutos. Consumo de batería: {consumo}%")
        else:
            print(f"Aplicación '{nombre}' no encontrada.")

    def mostrar_bateria(self):
        """
        Muestra el porcentaje de batería restante.
        """
        print(f"Batería: {self.__bateria}%")

# Ejemplo de uso

app1 = Celular("Facebook", 100)
app2 = Celular("Instagram", 150)

app1.instalar_aplicacion()
app2.instalar_aplicacion()

app1.utilizar_aplicacion("Facebook", 30)
app2.utilizar_aplicacion("Instagram", 45)

app1.mostrar_bateria()
app2.mostrar_bateria()