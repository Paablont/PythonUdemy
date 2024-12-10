#Basicamente para ver los indices sin necesidad de declarar una variable
lista = ['a','b','c']
indice = 0

for i in lista:
    print(indice,i)
    indice += 1

#Lo mismo, pero con enumerador mucho mas eficiente
for i in enumerate(lista):
    print(i)

#lista formada por tuplas
cadena = "Python"

lista_indices = list(enumerate(cadena))

print(lista_indices)


