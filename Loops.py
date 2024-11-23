lista = [1,2,3,4,5]

#podemos poner i como letra, lo que sea. Es el iterable
for i in lista:
    numero = lista.index(i)
    print('Numero',i, ' indice', numero)

print()
lista2 = ['pablo','luis','laura','fede','julia']

for nombre in lista2:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print(f'{nombre} no comienza por l')

print()
numeros = [1,2,3,4,5]
valor = 0
for num in numeros:
    valor = valor + num

print(valor)

#iterar en lista que tenga lista por ejemplo
for obj in [[1, 2], [3, 4], [5, 6]]:
    print(obj)

print()
for  a,b in [[1, 2], [3, 4], [5, 6]]:
    print(a) #recorre el primer indice
    print(b) #recorre el segundo

print()
#diccionarios
dic = {'clave1':'a','clave2':'b','clave3':'c'}

#solo claves
for i in dic:
    print(i)

#dic completo
for i in dic.items():
    print(i)
#dic solo valores
for i in dic.values():
    print(i)
#o tambien
for  a,b in dic.items():
    print(a,b) #recorre el primer indice
