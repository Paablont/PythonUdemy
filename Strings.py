#Una cadena siempre empieza en indice 0.
#De izq a derecha (imaginemos la palabra Hola): 0-H o-1 l-2 a-3 es decir 0 ... n
#De drc a izq: 0-H o--3 l--2 a--1 (es decir, 0 -n .... -1
cadena = 'Hola que tal'

resultado = cadena[3] #tendra el o

print("EL indice 3 es",resultado)

#Buscar el indice de un caracter en la cadena
#Si no existe, saldria error. Solo se pueden buscar un caracter (podemos buscar palabras, pero solo nos dara la pos de la primera letra de esa palabra)
resultado = cadena.index('a')
print("La letra a esta en la posicion: ",resultado)

#Como siempre busca de izq a derecha y se detiene al encontrar el primer caracter, se puede buscar en un rango especifico
resultado = cadena.index('a',5,11)
print('Del caracter 5 al 11, la letra a se encuentra en la posicion',resultado)

#Otra alternativa a index (busca al reves, de drc a izq)
resultado = cadena.rindex('a')
print('Con rindex, la primera posicion donde aparece la letra a es: ',resultado)

#Slicing, extraer una palabra de una cadena
print('+++++++ SLICING ++++++')
texto = 'ABCDEFGHIJKLMN'

fragmento = texto[2:10] #Extra todos los caracteres desde el indice 2 hasta (sin incluir) el 10
fragmento2 = texto[:10] #Igual pero extrae desde el inicio
fragmento3 = texto[2:10:2] #Extrae, pero cada 2 caracteres
fragmento4 = texto[::-1] #Toda la cadena pero al reves

print(fragmento)
print(fragmento2)
print(fragmento3)
print(fragmento4)

print('++++++++ METODOS ESENCIALES ++++++')
frase = 'Hola amigos que tal están'
#aparte del upper(), lower() que se pueden poner donde sea (imagina frase[3].upper() sacara el caracter de la pos 3 pero en mayus, etc)
#find es igual que index pero SI NO ENCUENTRA, devuelve -1 (util para condiciones)
print(frase.split()) #Saca todo pero en una lista segun el separador que se le ponga en el (), si no se le pone nada, sera el espacio en blanco
print(frase.split('a')) #Separa por el a PERO NO LO COGE OBVIAMENTE

#propiedad legth
print('Esta frase tiene ' ,len(frase) , 'caracteres')

#replace
frase = 'Esta frase es para remplazar cosas'
print(frase.replace('a','A'))
#No puedes cambiar el contenido de un string porque son inmutables. No podriamos hacer un frase[3] = 'D' donde cambiariamos la pos 3 por una D

a = 'Aprender'
b = 'Python'
c = 'es'
d = 'genial'
e = " ".join([a,b,c,d]) #siendo el caracter entre "" el separador
print(e)
e = "-".join([a,b,c,d]) #Separador por -
print(e)

#puedes multiplicar strings con *
texto = 'Hola ' *12
print(texto)

frase_espacios = """Hola amigos que tal estan
aqui es otro
salto de linea"""
#Buscar (devuelve true or false)
frase='Esta frase contiene un hola amigos'
print('hola' in frase)
