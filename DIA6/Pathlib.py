from pathlib import Path,PureWindowsPath
#Con pathlib es mucho mas eficiente
carpeta = Path("C:/Users/Pablo/PythonProjects/PythonUdemy/DIA6/pruebaPathLib/prueba.txt")
carpetasss = Path("C:/Users/Pablo/PythonProjects/PythonUdemy/DIA6/pruebaPathLib/pruebasss.txt")
#No hace falta abrir ni cerrar el archivo
print(carpeta.read_text())

#Por ejemplo para evitar errores
if not carpeta.exists():
    print('Este archivo no existe')
else:
    print(f'Nombre del archivo: ',carpeta.name)
if not carpetasss.exists():
    print('Este archivo no existe')
else:
    print(f'Nombre del archivo: ',carpeta.name)

print(carpeta.suffix)
print(carpeta.stem)

#Para adapptarse al formato de windows (esto da un poco igual porque teniendo Path se adapata a cualquier SO)
ruta = PureWindowsPath(carpeta)

print(ruta)