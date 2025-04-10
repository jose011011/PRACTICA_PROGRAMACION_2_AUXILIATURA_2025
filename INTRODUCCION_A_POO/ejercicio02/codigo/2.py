class Coche:
    def __init__(self,marca,modelo,velocidad):
        self.marca=marca
        self.modelo=modelo
        self.velocidad=velocidad
    def acelerar(self):
        aumen=self.velocidad+10
        return f'aumento la velocidad mas 10velocidad de modelo {self.modelo}: ',aumen
    def fenar(self):
        frena=self.velocidad-5
        return f"freno el cohe la velociada rebajo 5velocidad del modelo {self.modelo}: ",frena
    def __str__(self):
        return f"el coche de marca {self.marca} y modelo {self.modelo} va a una velocidad de {self.velocidad}"
    
ch1=Coche("toyota",2000,45)
ch2=Coche("Nissan",2010,35)
print(ch1)
print(ch2)
print("-"*20,"aceleracio","-"*20)
c1=ch1.acelerar()
c2=ch2.acelerar()
print(c1)
print(c2)
print("-"*20,"freno","-"*20)
co1=ch1.fenar()
co2=ch2.fenar()
print(co1)
print(co2)