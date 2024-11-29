import os

#get current working directory
ruta = os.getcwd()
print(ruta)
#cambiar de ruta a la que deseamos (en este caso rutas)
ruta_nueva = os.chdir('C:\\Users\\pvillasenor\\PythonProjects\\PythonUdemy\\DIA6\\rutas')
print(ruta_nueva)
archivo = open('rutas.txt')
print(archivo.read())

#crear carpeta
#ruta2 = os.makedirs('C:\\Users\\pvillasenor\\PythonProjects\\PythonUdemy\\DIA6\\rutas\\CarpetaNueva')


#recibir la ruta y el archivo por separado
ruta3 = 'C:\\Users\\pvillasenor\\PythonProjects\\PythonUdemy\\DIA6\\rutas\\rutas.txt'

elemento = os.path.basename(ruta3)
#tambien con .dirname o si quieres recibir ambos elementos pero separado
#.split, primero tendra el nomhre del directorio y luego el nombre de basename
#borrar carpetas rmdir y la ruta
os.rmdir('C:\\Users\\pvillasenor\\PythonProjects\\PythonUdemy\\DIA6\\rutas\\CarpetaNueva') #borra la carpeta que hemos creado en la linea 13

print(elemento)

#hay otra manera mejor de ver las rutas y manejar connellas (archivo Path.py)

