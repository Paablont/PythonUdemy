class Pajaro:
    #Atributos de clase serán iguales para todos los objetos de Pajaro (a diferencia de los del constructor que a lo mejor
    #pueden cambiar
    alas = True
    #Constructor para declarar atributos de Instancia
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    #Metodos de Instancia
    def piar(self):
        print(f'PIO PIO. Mi color es {self.color}')

    def volar(self,metros):
        print(f'El pajaro vuela {metros} m')
        self.piar()

    def pintar_negro(self):
        self.color = 'NEGRO'
        print('Ahora el pajaro es de color ',self.color)

    #Metodos de clase (no es necesario declarar un objeto de tipo la clase ni tampoco pueden acceder a los atr de Instancia
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'Puso {cantidad} huevos y tiene alas? {cls.alas}')

    #Metodos estaticos no pueden modificar atr de clase ni de instancia
    @staticmethod
    def mirar():
        print('El pajaro mira')


mi_pajaro = Pajaro('ROJO','Tucán')

#aqui seria lo tipico de mi_pajaro.atributos...
print(f'El pajaro {mi_pajaro.especie} es de color {mi_pajaro.color} y tiene alas?: {Pajaro.alas}')
print()
mi_pajaro.piar()
print()
mi_pajaro.volar(30)
mi_pajaro.pintar_negro()
print()
#Los metodos de clase no necesitan instancia
Pajaro.poner_huevos(5)
#Esto daria error: Pajaro.volar(30)
Pajaro.mirar() #Como no puede interacturar con atr de clase ni instancia, puede llamarlo la propia clase sin hacer un objeto de ese tipo

