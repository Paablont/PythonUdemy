#los de __ (por ejeplo el toString..
class CD:

    def __init__(self,autor,titulo,canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        return f'Album: {self.titulo} de {self.autor}'

    def __len__(self):
        return self.canciones

    def __del__(self):
        print('Se ha eliminado el CD')
mi_cd = CD('Pink Floyd','The Wall',24)
#Si no tuvieramos el str (ToString) saldria algo raro al llamar al objeto
print(mi_cd)
#con el len establecemos el largo del objeto (en este caso, el num de canciones, como si fuera una lista pero sin serlo)
print(f'Este cd tiene {len(mi_cd)}')

#eliminar alguna instancia.
#Como no notifica si elimina o no la instancia, es bueno hacer el __del__
del mi_cd
