class Catalogo:
    def __init__(self):
        self.elementos = []

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def buscar(self, criterio):
        return [e for e in self.elementos if criterio.lower() in str(e).lower()]

    def mostrar_todos(self):
        for e in self.elementos:
            print(e)

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"Libro: '{self.titulo}' por {self.autor}"

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre} - ${self.precio:.2f}"

print("Catálogo de Libros:")
catalogo_libros = Catalogo()
catalogo_libros.agregar(Libro("Cien Años de Soledad", "Gabriel García Márquez"))
catalogo_libros.agregar(Libro("El Principito", "Antoine de Saint-Exupéry"))
catalogo_libros.mostrar_todos()

print("\nBuscando 'Prin':")
for libro in catalogo_libros.buscar("Prin"):
    print(libro)

print("\nCatálogo de Productos:")
catalogo_productos = Catalogo()
catalogo_productos.agregar(Producto("Laptop", 1500))
catalogo_productos.agregar(Producto("Ratón inalámbrico", 25))
catalogo_productos.mostrar_todos()

print("\nBuscando 'laptop':")
for producto in catalogo_productos.buscar("laptop"):
    print(producto)
