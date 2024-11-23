#Combina 2 o mas listas entrelazando sus elementos en tuples
nombres = ['Ana','Hugo','Valeria']
edades = [65,40,28]
#zip solo llega al largo de la lista mas corta (si tenemos una lista de 3 y otra de 10, solo recorrera hasta la de 3

combinados = list(zip(nombres,edades))

print(combinados)

#Algo de utilidad
for nombre,edad in combinados:
    print(f'{nombre} tiene {edad} años')
