archivo = open('mi_archivo.txt','w') #abrimos en modo escritura

archivo.write('Nuevo texto') #escribimos

archivo = open('mi_archivo.txt','r') #abrimos en modo lectura

print(archivo.read()) #leemos

archivo.close() #cerramos

