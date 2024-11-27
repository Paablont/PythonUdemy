#Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se entregan, y devuelva esa cantidad como resultado

def cantiddad_atributos(**kwargs):
    return len(kwargs)
kwargs = {'valor1':23,'valor2':34,'valor3':43}
resultado = cantiddad_atributos(**kwargs)

print(f'Hay {resultado} parametros')


#Crea una función llamada devolver_distintos() que reciba 3 integers como parámetros
def devolver_distintos(*args):
    suma_numeros = sum(args)
    #Con funciones
    maximo, minimo = max(args), min(args)
    inter = sum(args) - maximo - minimo

    resultado = 0
    if suma_numeros > 15:
        resultado = maximo
    if suma_numeros < 10:
        resultado = minimo
    if 10 <= suma_numeros <= 15:
        resultado = inter

    return resultado

lista_numeros = [1,3,8,2]
valor = devolver_distintos(*lista_numeros)
print(valor)

#Escribe una función que requiera una cantidad indefinida de
#argumentos. Lo que hará esta función es devolver True si en
#algún momento se ha ingresado al numero cero repetido dos
#veces consecutivas
def repetido(*args):
    for i in range(len(args) - 1):
        if args[i] == args[i + 1]:
            return True
    return False

print(repetido(1, 2, 3, 0, 0, 1, 2))  # Esto debería devolver True.

print(repetido(1, 2, 3, 0, 0, 1, 2))  # Esto debería devolver True.

