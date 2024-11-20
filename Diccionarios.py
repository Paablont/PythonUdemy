#NO TIENEN INDICES/ORDEN. SON MUTABLES
#LAS CLAVES NO PUEDEN REPETIRSE, LOS VALORES SI
#LAS CLAVES PUEDEN SER TANTO NUMERICAS COMO ALFABETICAS, LOS VALORES PUEDEN SER CUALQUIER TIPO (HASTA OTROS DIC, LISTAS...)
diccionario = {'c1':'valor1','c2':'valor2'}

print(type(diccionario))
print(diccionario)

#CONSULTAR UN VALOR
resultado = diccionario['c1']
print(resultado)

#CASO VIDA REAL
cliente = {
        'nombre':'Pablo',
        'apellido':'Villaseñor',
        'peso':58,
        'talla':1.73
}
consulta = cliente['peso']
print(consulta)

#pueden contener de toda (diccionario dentro de diccionario, listas dentro de diccionarios ...)
dic = {'c1':55,'c2':[10,20,'wenisimo'],'c3':{'s1':100,'s2':200}}
print(dic['c2']) #imprime todos los valores que tenga c2
print(dic['c2'][2]) #lo mismo para el diccionario

#EJERCICIO. En una sola line de codigo una orden que imprima en pantalla la letra e pero en MAYUSCULA
dic = {'c1':['a','b','c'],'c2':['d','e','f']}
print(dic['c2'][1].upper())

#AGREGAR ELEMENTOS A UN DICCIONARIO
dic1 = {1:'a',2:'b'}
print(dic1)
dic1[3] = 'c'
print(dic1)

#SABES TODAS LAS CLAVES O VALORES O TODO A LA VEZ, metodo keys()
print(dic1.keys())
print(dic1.values())
print(dic1.items()) #esos parentesis son las TUPLES
