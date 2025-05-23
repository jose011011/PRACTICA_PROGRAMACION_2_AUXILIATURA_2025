class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        print(f"Producto: {self.nombre}, Precio: ${self.precio:.2f}")


    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def get_precio(self):
        return self.precio

    def set_precio(self, nuevo_precio):
        self.precio = nuevo_precio
class CarritoCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if len(self.productos) < 10:
            self.productos.append(producto)
            print(f"Producto '{producto.get_nombre()}' agregado al carrito.")
        else:
            print("El carrito ya tiene 10 productos. No se pueden agregar más.")

    def mostrar_carrito(self):
        print("🛒 Carrito de Compras:")
        if not self.productos:
            print("El carrito está vacío.")
        else:
            for prod in self.productos:
                prod.mostrar_info()


    def get_productos(self):
        return self.productos

    def set_productos(self, nueva_lista):
        if len(nueva_lista) <= 10:
            self.productos = nueva_lista
        else:
            print("No se puede asignar más de 10 productos.")
p1 = Producto("Manzana", 1.50)
p2 = Producto("Pan", 0.80)
p3 = Producto("Leche", 2.20)
p4 = Producto("Queso", 3.50)
p5 = Producto("Huevos", 1.90)
p6 = Producto("Jugo", 2.00)
p7 = Producto("Arroz", 1.30)
p8 = Producto("Azúcar", 1.10)
p9 = Producto("Sal", 0.70)
p10 = Producto("Aceite", 4.00)
p11 = Producto("Cereal", 3.00) 

carrito = CarritoCompras()
productos_a_agregar = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11]

for producto in productos_a_agregar:
    carrito.agregar_producto(producto)

carrito.mostrar_carrito()
