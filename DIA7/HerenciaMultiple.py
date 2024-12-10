class Padre:
    def hablar(self):
        print('Hola')
    pass

class Madre:
    def reir(self):
        print('jajaja')

    def hablar(self):
        print('Que tal?')

#Por ejemplo el metodo hola se repite en los 2 padres. Solo mostrará el de clase Padre ya que la herencia
#tiene un orden (es decir que si pusieramos Madre primero, heredaria el jajaja
class Hijo(Padre,Madre):
    pass

class Nieto(Hijo):
    pass

nieto = Nieto()
nieto.hablar()
nieto.reir()