from pathlib import Path

#ruta absoluta
base = Path.home()
#Construir una ruta con path
guia = Path(base,'Barcelona','Sagrada Familia.txt')
#cambiar el archivo de destino
guia2 = guia.with_name('Las ramblas.txt')
print(base)
print(guia) #No es una ruta, pero construye una posible ruta
print(guia2)
print()
guia_europa = Path(Path.home(),'Europa')
#los path son iterables
#Este for solo recorrera los archivos .txt de la carpeta Europa
for i in Path(guia_europa).glob('*.txt'):
    print(i)

print()
#Para iterar toda la carpeta
for i in Path(guia_europa).glob('**/*.txt'):
    print(i)