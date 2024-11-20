#SON MUTABLES
mi_lista = ['a','b','c']
otra_lista = ['hola',5,'PABLO',5.4] #Las listas en Python, a diferencia de otros lenguajes pueden contener distintos tiposd e datos
print(type(mi_lista))
#Todo lo de strings e indices se aplica en lista obvio
res = len(otra_lista)
print(res)

mi_lista2 = ['d','e','f']

mi_lista3 = mi_lista + mi_lista2
print(mi_lista3)

#esto en strings da error porque son INMUTABLES, las litas no
mi_lista3[0] = 'ALPHA'
print(mi_lista3)

mi_lista3.append('g')
print(mi_lista3)
mi_lista3.pop(3) #elimina el elemento que le pongas de indice (en este caso d). Si no pones nada, quitará el último
print(mi_lista3)
elemento_eliminado = mi_lista3.pop(2)
print(mi_lista3)
print('El elemento eliminado es: ', elemento_eliminado)

#ordenar listas
lista_sin_ordenar = ['g','a','z','b']
lista_sin_ordenar.sort() #no devuelve nada, es decir no puedes guardarla en una variable
sort = lista_sin_ordenar.sort()
print(lista_sin_ordenar)
lista_sin_ordenar.reverse()
print(lista_sin_ordenar)
print(sort) #por eso muestra none