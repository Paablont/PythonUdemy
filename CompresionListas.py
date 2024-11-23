#Manera dinamica de construir listas (algo mas eficiente). Imagina construir una lista con .append, pues mas eficiente

palabra = 'python'

lista = []
for i in palabra:
    lista.append(i)

print(lista)

#Eficiente con la compresion
#Una letra por cada letra que haya en palabra
lista_nueva = [i for i in palabra]

print(lista_nueva)

#Otros ejemplos
lista_rangos = [n for n in range(0,21,2) if n * 2 > 10]

print(lista_rangos)

#si ponemos else, debe ir delante del for
lista_rangos = [n if n * 2 > 10 else 'no' for n in range(0,21,2)]

print(lista_rangos)

#Mini ejercicio
pies = [10,20,30,40,50]
metros =[] #Obtener una lista compuesta de pies a metros, *3.281

metros_resuelto = [pie * 3.281 for pie in pies]
print(metros_resuelto)