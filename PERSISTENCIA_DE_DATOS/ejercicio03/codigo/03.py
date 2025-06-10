
class Medicamento:
    def __init__(self, nombre, codMedicamento, tipo, precio):
        self.nombre = nombre
        self.codMedicamento = codMedicamento
        self.tipo = tipo
        self.precio = precio

    def leer(self):
        return f"{self.nombre},{self.codMedicamento},{self.tipo},{self.precio}"

    def getTipo(self):
        return self.tipo

    def getPrecio(self):
        return self.precio

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - Bs {self.precio}"


class Farmacia:
    def __init__(self, nombreFarmacia, sucursal, direccion, nit, medicamentos=None):
        self.nombreFarmacia = nombreFarmacia
        self.sucursal = sucursal
        self.direccion = direccion
        self.nit = nit
        self.medicamentos = medicamentos if medicamentos else []

    def mostrar(self):
        print(f"Farmacia: {self.nombreFarmacia} | Sucursal: {self.sucursal} | Dirección: {self.direccion}")
        for med in self.medicamentos:
            print(f"  - {med}")

    def getSucursal(self):
        return self.sucursal

    def getDireccion(self):
        return self.direccion

    def getMedicamentos(self):
        return self.medicamentos

    def buscaMedicamento(self, nombreMedicamento):
        for med in self.medicamentos:
            if med.nombre.lower() == nombreMedicamento.lower():
                return True
        return False

    def leer(self):
        data = f"{self.nombreFarmacia},{self.sucursal},{self.direccion},{self.nit}\n"
        for med in self.medicamentos:
            data += f"{med.leer()}\n"
        data += "---\n" 
        return data


class ArchFarmacia:
    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo

    def crearArchivo(self):
        with open(self.nombreArchivo, "w") as f:
            pass 

    def adicionar(self, farmacia):
        with open(self.nombreArchivo, "a") as f:
            f.write(farmacia.leer())

    def mostrar(self):
        farmacias = self.leerFarmacias()
        for f in farmacias:
            f.mostrar()
            print()

    def leerFarmacias(self):
        farmacias = []
        try:
            with open(self.nombreArchivo, "r") as f:
                lines = f.readlines()
                i = 0
                while i < len(lines):
                    if lines[i].strip() == '':
                        i += 1
                        continue
                    if lines[i].strip() == "---":
                        i += 1
                        continue
                    datos = lines[i].strip().split(",")
                    nombreFarmacia, sucursal, direccion, nit = datos
                    i += 1
                    medicamentos = []
                    while i < len(lines) and lines[i].strip() != "---":
                        nombre, cod, tipo, precio = lines[i].strip().split(",")
                        medicamentos.append(Medicamento(nombre, int(cod), tipo, float(precio)))
                        i += 1
                    farmacia = Farmacia(nombreFarmacia, int(sucursal), direccion, int(nit), medicamentos)
                    farmacias.append(farmacia)
        except FileNotFoundError:
            print("Archivo no encontrado.")
        return farmacias

    def mostrarMedicamentosTos(self, sucursal):
        farmacias = self.leerFarmacias()
        for f in farmacias:
            if f.getSucursal() == sucursal:
                print(f"Medicamentos para la tos en la sucursal {sucursal}:")
                for m in f.getMedicamentos():
                    if m.getTipo().lower() == "tos":
                        print(f"  - {m.nombre} Bs{m.getPrecio()}")
                break

    def buscarMedicamentoEnFarmacias(self, nombreMedicamento):
        farmacias = self.leerFarmacias()
        for f in farmacias:
            if f.buscaMedicamento(nombreMedicamento):
                print(f"El medicamento '{nombreMedicamento}' está en la sucursal {f.getSucursal()}, dirección: {f.getDireccion()}")
archivo = ArchFarmacia("farmacias.txt")
archivo.crearArchivo()

meds1 = [
    Medicamento("Paracetamol", 101, "fiebre", 3.5),
    Medicamento("Mucosolvan", 102, "tos", 5.0),
    Medicamento("Golpex", 103, "tos", 7.0),
]
meds2 = [
    Medicamento("Ibuprofeno", 104, "dolor", 4.0),
    Medicamento("Golpex", 105, "tos", 6.5),
]

f1 = Farmacia("Farmacia Central", 1, "Av. Siempre Viva", 123456, meds1)
f2 = Farmacia("Farmacia Moderna", 2, "Calle Falsa 123", 654321, meds2)

archivo.adicionar(f1)
archivo.adicionar(f2)

archivo.mostrar()

archivo.mostrarMedicamentosTos(1)

archivo.buscarMedicamentoEnFarmacias("Golpex")
