# La consigna es esta: el programa le va a preguntar al usuario su nombre, y luego le va a decir
# algo así como “Bueno, Juan, he pensado un número entre 1 y 100, y tienes solo ocho intentos
# para adivinar cuál crees que es el número”. Entonces, en cada intento el jugador dirá un
# número y el programa puede responder cuatro cosas distintas:
#  Si el número que dijo el usuario es menor a 1 o superior a 100, le va a decir que ha elegido
# un número que no está permitido.
#  Si el número que ha elegido el usuario es menor al que ha pensado el programa, le va a
# decir que su respuesta es incorrecta y que ha elegido un número menor al número secreto.
#  Si el usuario eligió un número mayor al número secreto, también se lo hará saber de la
# misma manera.
#  Y si el usuario acertó el número secreto, se le va a informar que ha ganado y cuántos
# intentos le ha tomado.
# Si el usuario no ha acertado en este primer intento, se le va a volver a pedir que elija otro
# número. Y así hasta que gane o hasta que se agoten los ocho intentos.
import random

intentos= 8
acertado = False
nombre = input('Hola, escribe tu nombre ')
numero_aleatorio = random.randint(1,10)
print(f'numero aleatorio: {numero_aleatorio}')
print(f'Hola {nombre}. He pensado un número entre el 1 y el 10. Tienes {intentos} intentos para adivinarlo')


while intentos > 0 and not acertado:
    numero_usuario = int(input('Introduce un número '))
    if not (0 < numero_usuario < 11):
        print('Por favor, introduce un rango entre el 1 y 10')
        continue #Salta a la siguiente iteracion (reinicia el bucle)
    elif numero_usuario < numero_aleatorio:
        intentos -= 1
        print(f'El número que has elegido es menor que el número programado. Te quedan {intentos} intentos ')
    elif numero_usuario > numero_aleatorio:
        intentos -= 1
        print(f'El número que has elegido es mayor que el número programado. Te quedan {intentos} intentos ')
    else:
        print('Has acertado!')
        acertado = True
else:
    print('Fin del juego')

