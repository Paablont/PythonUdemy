class Animal:

    def __init__(self,nombre,color):
        self.nombre = nombre
        self.color = color

    def nacer(self):
        print('Este animal ha nacido')
    pass

    def hablar(self):
        print('Este animal emite un sonido')

class Pajaro(Animal):

    def __init__(self,nombre,color,altura_vuelo):
        super().__init__(nombre,color) #Para hererar el init de Animal
        self.altura_vuelo = altura_vuelo
    def hablar(self):
        print('pio')
    pass

print(Pajaro.__bases__) #De quien hereda?
print(Animal.__subclasses__()) #Que hereda

mi_pajaro = Pajaro('Piolin','Amarillo',60)
mi_animal = Animal('ANimal1','Negro')
mi_pajaro.nacer()
print(f'El pájaro {mi_pajaro.nombre} es de color {mi_pajaro.color}')
mi_animal.hablar()