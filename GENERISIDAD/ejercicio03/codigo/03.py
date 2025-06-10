class Pila:
    def __init__(self):
        self.elementos = []
    
    def apilar(self, elemento):
        self.elementos.append(elemento)
    
    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        return None
    
    def esta_vacia(self):
        return len(self.elementos) == 0
    
    def mostrar(self):
        print("Contenido de la pila:", self.elementos)

pila_enteros = Pila()
pila_enteros.apilar(10)
pila_enteros.apilar(20)
pila_enteros.apilar(30)
pila_enteros.mostrar()
print("Desapilado:", pila_enteros.desapilar())
pila_enteros.mostrar()

pila_cadenas = Pila()
pila_cadenas.apilar("Python")
pila_cadenas.apilar("Java")
pila_cadenas.apilar("C++")
pila_cadenas.mostrar()
print("Desapilado:", pila_cadenas.desapilar())
pila_cadenas.mostrar()