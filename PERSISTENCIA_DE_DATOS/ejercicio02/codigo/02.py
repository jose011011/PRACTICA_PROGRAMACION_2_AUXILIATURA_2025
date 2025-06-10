
class Cliente:
    def __init__(self, id, nombre, telefono):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"{self.id},{self.nombre},{self.telefono}"

    @staticmethod
    def desde_texto(linea):
        id, nombre, telefono = linea.strip().split(',')
        return Cliente(int(id), nombre, int(telefono))

class ArchivoCliente:
    def __init__(self, nomA):
        self.nomA = nomA

    def crearArchivo(self):
        with open(self.nomA, 'w') as archivo:
            pass
        print("Archivo creado correctamente.")

    def guardarCliente(self, cliente):
        with open(self.nomA, 'a') as archivo:
            archivo.write(str(cliente) + '\n')
        print(f"Cliente {cliente.nombre} guardado con éxito.")

    def cargarClientes(self):
        clientes = []
        try:
            with open(self.nomA, 'r') as archivo:
                for linea in archivo:
                    clientes.append(Cliente.desde_texto(linea))
        except FileNotFoundError:
            print("El archivo no existe.")
        return clientes

    def buscarCliente(self, c):
        clientes = self.cargarClientes()
        for cli in clientes:
            if cli.id == c:
                return cli
        return None

    def buscarCelularCliente(self, c):
        clientes = self.cargarClientes()
        for cli in clientes:
            if cli.telefono == c:
                return cli
        return None
archivo = ArchivoCliente("clientes.txt")
archivo.crearArchivo()
archivo.guardarCliente(Cliente(1, "José", 76543210))
archivo.guardarCliente(Cliente(2, "Lucía", 72345678))
archivo.guardarCliente(Cliente(3, "Mario", 71234567))
cli = archivo.buscarCliente(2)
if cli:
    print("Cliente encontrado por ID:", cli.nombre, cli.telefono)
else:
    print("Cliente no encontrado.")
cliCel = archivo.buscarCelularCliente(71234567)
if cliCel:
    print("Cliente encontrado por celular:", cliCel.nombre, cliCel.telefono)
else:
    print("No hay cliente con ese número.")
