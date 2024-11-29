archivo = open('prueba.txt', 'w') #la W reescribe, la a escribe desde el final del archivo (ultima linea escrita)
archivo.write('''escrito desde python'
'que tal''') #para saltos de linea 3 comillas al comienzo y final (cuidado con los espacios en blanco

#writeLines puedes pasar una lista de strings (que no escribe varias linea ojo)
archivo.writelines(['hola ','mundo','aqui','estoy'])

lista = ['HOLA ','mundo','aqui','estoy']
for p in lista:
    archivo.writelines(p + '\n')
archivo.close()

