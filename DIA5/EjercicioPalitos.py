from random import shuffle

#Juego de palitos al azar. Si te toca el palo pequeño pierdes
#funcion mezclar palos
def mezclar_palitos(palitos):
    shuffle(palitos)

#Comprobamos que lo mezcla
#mezclar_palitos(palitos)
#print(palitos)

# Pedir intento al usuario
def pedir_usuario():
    intento = 0
    while not (1 <= intento <= 4):  # Comprobar si el número está entre 1 y 4
        intento = int(input('Por favor, introduce un numero del 1 al 4: '))
    return intento

#Decir si lava o no
def resultado(palitos,intento):
    if palitos[intento-1] == '-':
        print('A FREGAR LOS PLATOS')
    else:
        print('Esta vez te salvas')

#Lista de palitos
palitos = ['-','--','---','----']
mezclar_palitos(palitos)
intento = pedir_usuario()

resultado(palitos,intento)
