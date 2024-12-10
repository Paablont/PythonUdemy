#SOLO ADMITEN ELEMENTOS UNICOS ( NO SE PUEDEN REPETIR ).
#NO TIENEN INDICES/ORGANIZARLOS
#LOS ELEMENTOS SON INMUTABLES. NO PUEDES METER LISTAS Y DICCIONARIOS

#varias formas de declararlo (pueden ser {} () o [])
mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)

otro_set = {1,2,3}
print(type(otro_set))
print(otro_set)

#buscar elementos
# print(mi_set[0]) error
# mi_set[0] = 5 error

#si metemos valores repetidos, no las cuenta
set_repetido = set([1,2,3,4,1,2,3,3,4,4])
print(set_repetido)

print(len(mi_set))
print(2 in set_repetido) #realmente esto se puede hacer con todos (los diccionarios solo buscando claves)

#juntar sets
s1 = {1,2,3,4}
s2 = {5,6,7,8}
s3 = s1.union(s2)
print(s3)

#agregar eliminar, limpiar
s1.add('hola')
print(s1)
s1.remove(3)
print(s1)
s1.discard(6) #es como remove, pero si el elemento no existe, no da fallo
s1.pop() #eliminara un elemento aleatorio, no el ultimo como en strings
print(s1)
s1.clear()
print(s1)
