class Estudiante:
    def __init__(self,nombre,nota_1,nota_2):
        self.nombre=nombre
        self.nota_1=nota_1
        self.nota_2=nota_2
    def Promedio(self):
        suma=(self.nota_1+self.nota_2)/2
        return "el promedio es: ",suma
    def Ver_aprobo(self):
        suma=(self.nota_1+self.nota_2)/2
        if suma>=61 and suma<=100:
            return f"el estudiante {self.nombre} APROBO la amteria"
        else:
            return f"el estudiante {self.nombre} REPROBO la amteria"
    def __str__(self):
        return f"nombre: {self.nombre} nota_1: {self.nota_1} nota_2: {self.nota_2}"
est1=Estudiante("jose",90,60)
est2=Estudiante("daniel",50,63)
est3=Estudiante("juan",79,40)
print(est1)
print(est2)
print(est3)
e1=est1.Promedio()
e2=est2.Promedio()
e3=est3.Promedio()
es1=est1.Ver_aprobo()
es2=est2.Ver_aprobo()
es3=est3.Ver_aprobo()
print(es1)
print(es1)
print(es3)