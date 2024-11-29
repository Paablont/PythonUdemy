mi_archivo = open('prueba.txt')

#para verlo en pantalla, lo metemos en un print
print(mi_archivo.read())

#print(mi_archivo.readline()) #Solo leeria una linea del .txt
#Si ponemos varios readline, leera linea por linea, no siempre leera la primera linea porque al final de cada readline, deja un "punto de guardado" de lectura
#Si no queremos mostrar ese salto de linea entre lineas, aplicamos el metodo .rstrip()

#Si usamos readlines(), devolvera una lista con cada linea en elementos seeparados. En este caso
#['Hola!','wwoow']

#Tambien podemos iterar un archivo
for linea in mi_archivo:
    print('Aqui comienza la linea que dice: ',linea)

#Esto se puede meter en variables, es decir
#texto = mi_archivo.read() y usar esa variabe

#Siempre cerrar el archivo al final de la ejecucion
mi_archivo.close()