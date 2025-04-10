class Persona:
    def __init__(self,nombre,edad,ciudad):
        self.nombre=nombre
        self.edad=edad
        self.ciudad=ciudad
    def motrar_saludo(self):
        return f"hola, soy {self.nombre} de {self.ciudad}"
    def es_mayor(self):
        if self.edad>=18:
            return f"es mayor de edad {self.nombre}"
        else:
            return f"no es mayor de edad {self.nombre}"
p1=Persona("jose",14,"La Paz")
p2=Persona("juan",20,"Santa Cruz")
p3=Persona("daniel",19,"El Alto")
pe1=p1.motrar_saludo()
pe2=p2.motrar_saludo()
pe3=p3.motrar_saludo()
print(pe1)
print(pe2)
print(pe3)
per1=p1.es_mayor()
per2=p2.es_mayor()
per3=p3.es_mayor()
print(per1)
print(per2)
print(per3)