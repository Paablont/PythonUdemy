from pathlib import Path

#Manejo de directorios MEJORADO. La diferencia principal es que esto es universal entre Linux, MAC y Windows

carpeta = Path('C:/Users/pvillasenor/PythonProjects/PythonUdemy/DIA6/rutas')

archivo = carpeta / 'rutas.txt'

#asi creamos la ruta completa
mi_archivo = open(archivo)
print(mi_archivo.read())