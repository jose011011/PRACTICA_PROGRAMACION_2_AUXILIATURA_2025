from typing import TypeVar, Generic

T = TypeVar('T')

class Caja(Generic[T]):
    def __init__(self):
        self._contenido = None
    
    def guardar(self, objeto: T) -> None:
        self._contenido = objeto
    
    def obtener(self) -> T:
        return self._contenido
caja_palabras = Caja[str]()
caja_palabras.guardar("Python Generics")
    
caja_numeros = Caja[int]()
caja_numeros.guardar(3.1416)
    
print(f"Caja 1 contiene: {caja_palabras.obtener()}")
print(f"Caja 2 contiene: {caja_numeros.obtener()}")
    
caja_compleja = Caja[dict]()
caja_compleja.guardar({"nombre": "Python", "version": 3.12})
print(f"Caja 3 contiene: {caja_compleja.obtener()}")