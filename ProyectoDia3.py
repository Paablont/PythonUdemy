#La consigna es la siguiente: vas a crear un programa que primero le pida al usuario que
#ingrese un texto. Puede ser un texto cualquiera: un artículo entero, un párrafo, una frase, un
#poema, lo que quiera. Luego, el programa le va a pedir al usuario que también ingrese tres
#letras a su elección y a partir de ese momento nuestro código va a procesar esa información
#para hacer cinco tipos de análisis y devolverle al usuario la siguiente información:

#Primero: ¿cuántas veces aparece cada una de las letras que eligió?
#Segundo: le vas a decir al usuario cuántas palabras hay a lo largo de todo el texto.
#Tercero: nos va a informar cuál es la primera letra del texto y cuál es la última.
#Cuarto: el sistema nos va a mostrar cómo quedaría el texto si invirtiéramos el orden de las palabras.
#Quinto: el sistema nos va a decir si la palabra “Python” se encuentra dentro del texto

frase_usuario = input('Por favor, escriba una frase para comenzar el programa ').lower()
#Las letras podrian ir en una lista, añadiendo con .append y luego [indice] para buscar la letra
l1 = input('Escriba una primera letra ').lower()
l2 = input('Escriba una segunda letra ').lower()
l3 = input('Escriba una tercera letra ').lower()

#Primero
#Se podría hacer en string también con el mismo metodo pero sin pasarloa  lista
lista_frase = list(frase_usuario)
print(f'la letra {l1} aparece {lista_frase.count(l1)} veces')
print(f'la letra {l2} aparece {lista_frase.count(l2)} veces')
print(f'la letra {l3} aparece {lista_frase.count(l3)} veces')

#Segundo
palabras = frase_usuario.split()
print(f"Hemos encontrado {len(palabras)} palabras en tu texto")
#Si lo hago sin split, cuenta letra por letra

#Tercero
tupla_frase = tuple(frase_usuario)
print(f'La primera letra de la frase es {tupla_frase[0]}, la última {tupla_frase[-1]}')

#Cuarto
frase_reves = " ".join(frase_usuario.split()[::-1])
print(frase_reves)

#Quinto
print(f'¿La palabra "python" aparece en la frase? {'python' in frase_usuario}')