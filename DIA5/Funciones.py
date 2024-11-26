#PYTHON LEE DE ARRIBA A ABAJO, SI CREO UNA FUNCION ABAJO Y LA USO ARRIBA, NO EXISTIRA (ejemplo)
#numero1 = 10
#numero2 = 20
# variable1 = sumaNumeros(numero1,numero2)
#funcion sumaNumeros. ESTO NO EXISTIRÁ PORQUE LA FUNCION DEBE IR ANTES

#Ejemplo bien hecho
num1 = 2
num2 = 10

def sumarNumeros(numero1,numero2):
    suma = numero1 + numero2
    return suma

resultado = sumarNumeros(num1,num2)
print(resultado) #debe dar 12