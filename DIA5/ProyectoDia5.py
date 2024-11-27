import random
from random import choice

palabras = ['pablito','arbol','cama','sol']

palabra_oculta = random.choice(palabras)

print(f'MODO DEV: {palabra_oculta}')

#Metodo para mostrar los guiones según letras tenga la palabra
def mostrar_guiones(palabra):
    guiones = ''
    for i in palabra:
        print('_',end=' ')
    print()

#Metodo para comprobar si la letra esta en la palabra
def comprobar_letra(letra,palabra_oculta):
    if letra not in palabra_oculta:
        print('La letra no está en la palabra')
        return False
    else:
        pass
    return True



print(f'Bienvenido al juego del ahorcado. La palabra oculta es: ')

print()
vidas = 5
letra = ''
while vidas > 0:
        mostrar_guiones(palabra_oculta)
        print()
        letra_usuario = input('Introduce una letra ').lower()
        print()
        if not comprobar_letra(letra_usuario,palabra_oculta):
            vidas -= 1
            print(f'Te quedan {vidas} vidas')
        else:
            for i in palabra_oculta:
                if i == letra_usuario:
                    print(i, end=' ')
                else:
                    print('_', end=' ')
            print()
