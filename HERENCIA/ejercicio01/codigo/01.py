class Vehiculo:
    def __init__(self, marca, modelo, año, precio_base):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__precio_base = precio_base

    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_año(self):
        return self.__año

    def get_precio_base(self):
        return self.__precio_base

    def set_marca(self, marca):
        self.__marca = marca

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def set_año(self, año):
        self.__año = año

    def set_precio_base(self, precio):
        self.__precio_base = precio

    def mostrar_info(self):
        print(f'''
Marca: {self.__marca}
Modelo: {self.__modelo}
Año: {self.__año}
Precio base: ${self.__precio_base}
''')


class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, precio_base, num_puertas, tipo_combustible):
        super().__init__(marca, modelo, año, precio_base)
        self.__num_puertas = num_puertas
        self.__tipo_combustible = tipo_combustible

    def get_num_puertas(self):
        return self.__num_puertas

    def get_tipo_combustible(self):
        return self.__tipo_combustible

    def set_num_puertas(self, puertas):
        self.__num_puertas = puertas

    def set_tipo_combustible(self, combustible):
        self.__tipo_combustible = combustible

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de puertas: {self.__num_puertas}")
        print(f"Tipo de combustible: {self.__tipo_combustible}\n")


class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, precio_base, cilindrada, tipo_motor):
        super().__init__(marca, modelo, año, precio_base)
        self.__cilindrada = cilindrada
        self.__tipo_motor = tipo_motor

    def get_cilindrada(self):
        return self.__cilindrada

    def get_tipo_motor(self):
        return self.__tipo_motor

    def set_cilindrada(self, cilindrada):
        self.__cilindrada = cilindrada

    def set_tipo_motor(self, tipo):
        self.__tipo_motor = tipo

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Cilindrada: {self.__cilindrada}")
        print(f"Tipo de motor: {self.__tipo_motor}\n")

c1 = Coche("Toyota", "Corolla", 2025, 25000, 4, "Gasolina")
m1 = Moto("Yamaha", "MT-03", 2025, 5000, "321cc", "4 tiempos")
c1.mostrar_info()
m1.mostrar_info()

print("=== COCHES CON MÁS DE 4 PUERTAS ===")
for coche in [c1]:
    if coche.get_num_puertas() > 4:
        coche.mostrar_info()
print("=== VEHÍCULOS GESTIÓN 2025 ===")
for vehiculo in [c1, m1]:
    if vehiculo.get_año() == 2025:
        vehiculo.mostrar_info()
