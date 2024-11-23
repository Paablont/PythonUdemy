monedas = 5

while monedas > 0:
    print('Tengo ' ,monedas, ' monedas')
    monedas = monedas - 1 #o tambien monedas -= 1

#Tambien puede tener else
while monedas > 0:
    print('Tengo ' ,monedas, ' monedas')
    monedas = monedas - 1 #o tambien monedas -= 1
else:
    print('No tengo mas monedas')

respuesta = 's'
while respuesta == 's':
    respuesta = input('Quieres seguir? (s/n)').lower()
else:
    print('Gracias')

#funcion pass, break y continue
edad = 0
while edad == 0:
    pass

print('Pass funcion')