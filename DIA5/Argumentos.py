#Podemos definir funciones cuyo num de argumentos sea variado
#Se recomienda usar args pero podemos poner tanto args como otra palabra, lo importante es el *.
from PythonUdemy.DIA5.ArgumentosEjercicios import kwargs


#args seria: args = [100,2,3,4 ... n]

#funcion normal
def suma(a,b):
    return a+b

print(suma(4,7))

#funcion con args (parametros indefinidos)
def suma2(*args):
    #imagina que queremos sumar todos esos numeros (indefinidos)
    total = 0
    for i in args:
        total += i

    return total

print(suma2(2,3,4,112,13,4))
#o tambien
print(suma2(2,3,4))

#tambien existe la funcion sum porque como *args es una tupla, funciona
def suma3(*args):
    return sum(args)

lista = [2,3,4,5]
print(sum(lista))
tupla = (2,3,4,1)
print(sum(tupla))


def suma_cuadrados(*args):
    lista = []
    for i in args:
        lista.append(i*i)
    return sum(lista)

print(suma_cuadrados(1,2,3))

#**kwargs (key word args) por diccionarios
def claves(**kwargs):
    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')

claves(x=3,e=2,z=3,d=1)

#ORDEN DE ARGUMENTOS (valores normales,*args,**kwargs)

#kwargs seria: kwargs = { 'x':100,'y':200,'z':400 }

def suuuma(num1,num2,*args,**kwargs):
    print(f'El primer valor es: {num1}')
    print(f'El segundo valor es: {num2}')

    for i in args:
        print(f'Argumento = {i}')

    for i,j in kwargs.items():
        print(f'{i} = {j}')
#Ojo, el kwargs no se pasa como diccionario, si no como valores y variables
# se podria pasar como listas o dicionario el args y el kwargs, pero hay que poner los * delante
suuuma(14,25,2,56,4,2,x='palabra1',y='dos',z='tres')
#o por ejemplo
args = [1,3,4,2]
kwargs = {'valor1':2,'valor2':10}
suuuma(2,4,*args,**kwargs)