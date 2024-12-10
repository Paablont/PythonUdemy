#EN PYTHON NO USAR CAMELCASE, SI NO _ (miVariable NO, mi_variable)
#string, float, int bla bla listas [] bla, booleanos

#DICCIONARIOS (en grupos de 2, palabra y definicion)
print('DICCIONARIO')
midic = {'color':'rojo','arte':'cine','lista':[1,2,3,'valor']}
print(midic)

#Las tuples son como listas PERO SON INMUTABLES
#mitupla = (20,'Pablo',1234, 20, [una lista]) igual que los diccionarios puede tener de to

#set es un conjunto de elementos UNICOS (es decir en una lista puedes tener dos A, dos 2... aqui no)

#Asi puedo imprimir que tipo de dato es la variable
print(type(midic))

#Como printf en java, python tiene el format para imprimir (recuerda que en python no puedes meter en print un int con string y asi a no ser que
# castees y no es practico)
color = 'rojo'
numero = 2
print('El color {} es el numero {}'.format(color,numero)) #ESTA ES LA FORMA ANTIGUA ANTES DE PYTHON 6.0,

# LA NUEVA FORMA ES LA CADENA LITERAL
print(f'El color {color} es el numero {numero}')

#OPERADORES MATEMATICOS (tmbn se puede importar la libreria math para hacer mas cosas matematicas y mejor estructuradas
# Suma: +
# Resta: -
# Multiplicación: *
# División: /
# Cociente (división "al piso"): //
# Resto (módulo): % UTIL PARA DETECTAR VALORES PARES
# Potencia: **
# Raíz cuadrada: **0.5 y .sqrt

#Redondear (round(numero,decimales))

print(round(5+8.4,4))









