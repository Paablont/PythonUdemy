#Basicamente funciones mas complejas


def chequear_3_cifras(numero):
    return numero in range(100,1000)

resultado = chequear_3_cifras(658)
print(resultado) #Debe dar True

#Comprobar que en una lista hay algun numero de 3 cifras
def cheq_lista(lista):
    for n in lista:
        if n in range(100,1000):
            return True #Return aparte de devolver, tambien rompe el loop
        else:
            pass

lista = [1,4,234,6,33]

resultado = cheq_lista(lista)
print(resultado) #Devolveria true

#Esto seria un error tipico ya que si no tiene algun num de 3 cifras, la funcion no esta preparada para devolver un false. Corregida seria
def cheq_lista(lista):
    for n in lista:
        if n in range(100,1000):
            return True #Return aparte de devolver, tambien rompe el loop
        #Si tuvieramos variable, deberiamos poner un break. Es por eso que mejor directamente el return
        else:
            pass
    return False #Tambien podriamos usar una variable pero esto es algo mas personal

def devuelve_lista(lista):
    lista_numeros = []
    for n in lista:
        if n in range(100, 1000):
            lista_numeros.append(n)  # Return aparte de devolver, tambien rompe el loop
        else:
            pass
    return lista_numeros

lista2 = [1,4,234,6,333,234,10000,23]
resultado = devuelve_lista(lista2)
print(resultado)


#Miniejercicio
print('MINIEJERCICIO')
def todo_positivos(lista):
    for n in lista:
        if n < 0:
            return False
        else:
            pass
    return True

print(todo_positivos([1,45,12,8,6])) #True
print(todo_positivos([1,45,-1,8,6])) #False
