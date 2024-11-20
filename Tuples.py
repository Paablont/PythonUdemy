#SIMILAR  A LAS LISTAS PERO SON INMUTABLES (los elementos no). NO SE SUELEN USAR MUCHO EN LOS PRINCIPIANTES
#OCUPAN MENOS ESPACIO. SI NECESITAMOS ALGO EN ESPECIFICO QUE NO QUEREMOS MODIFICAR
mi_tuple = (1,2,3,4) #puede ir sin parentesis
print(type(mi_tuple))
print(mi_tuple)
mi_tuple_todo = ('hola',2,3.5,'bien') #puede tener de todo
print(type(mi_tuple_todo))
print(mi_tuple_todo)

print(mi_tuple[0]) #al igual que string, puede tener indices negativos
#mi_tuple[0] = 5 da error

#podemos anidar tuples igual que listas y dic
mi_tuple2 = (1,2,(10,20),4)
print(mi_tuple2[2])
print(mi_tuple2[2][0])

#casting tmbn
mi_tuple2 = list(mi_tuple)
print(type(mi_tuple2))
mi_tuple2 = tuple(mi_tuple)
print(type(mi_tuple2))

#asignar valores (se puede hacer con listas, diccionarios) SIEMPRE QUE COINCIDAN LA CANTIDAD DE VALORES Y VARIABLES
w,x,y,z = mi_tuple
print(w,x,y,z)

t = (1,2,3,1)
print(len(t))
print(t.count(1)) #Cantidad de apariciones de un valor dentro del tuple
print(t.index(2)) #indica el indice

