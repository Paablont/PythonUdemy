import random
from random import choice

palabras = ['pablito','arbol','cama','sol']

palabra_oculta = random.choice(palabras)

print(f'MODO DEV: {palabra_oculta}')

#Metodo para mostrar los guiones según letras tenga la palabra
def mostrar_guiones(palabra_oculta):
    lista_palabra = []
    for i in palabra_oculta:
        lista_palabra.append('_')
    return lista_palabra
#Esta bien pero podria hacerse con return ['_'] * len(palabra_oculta)

#Metodo para comprobar si la letra esta en la palabra
def comprobar_letra(letra,palabra_oculta):
    if letra not in palabra_oculta:
        print('La letra no está en la palabra')
        return False
    return True

def actualizar_palabra(letra_usuario,lista,palabra_oculta):
    for i,char in enumerate(palabra_oculta):
        if char == letra_usuario:
            lista_palabra[i] = letra_usuario


lista_palabra = mostrar_guiones(palabra_oculta)
print(f'Bienvenido al juego del ahorcado. La palabra oculta es: ')

vidas = 5

while vidas > 0:
        print("\n", " ".join(lista_palabra))  # Muestra el progreso actual de la palabra
        letra_usuario = input('Introduce una letra ').lower()
        print()
        if not comprobar_letra(letra_usuario,palabra_oculta):
            vidas -= 1
            print(f'Te quedan {vidas} vidas')
            if vidas == 0:
                print(f'Has perdido. La palabra secreta era: {palabra_oculta}')
                break
        else:
            palabra = actualizar_palabra(letra_usuario,lista_palabra,palabra_oculta)
        if '_' not in lista_palabra:
            print(f'¡Felicidades! Adivinaste la palabra: {palabra_oculta}')
            break