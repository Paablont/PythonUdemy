#saber cual es el cafe mas caro
from PythonUdemy.DIA5.Funciones import resultado


def cafe_mas_caro(precios):
    precio_mayor = 0
    cafe_caro = ''
    for cafe,precio in precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_caro = cafe
        else:
            pass

    return (cafe_caro,precio_mayor)
#Lista de precios de cafe
precios_cafe = [('capuchino',1.5),('Espresso',1.2),('Moka',1.9)]

resultado = cafe_mas_caro(precios_cafe)
print(f'El cafe mas caro es el {resultado[0]} con un precio de {resultado[1]}')
#o tambien se puede hacer (mas util siendo python)
cafe_caro,precio_car = cafe_mas_caro(precios_cafe)
print(f'El cafe mas caro es el {cafe_caro} con un precio de {precio_car}')

for i in precios_cafe:
    print(i)

#Formas de desempacar el tupple
for cafe,precio in precios_cafe:
    print(cafe)
    print(precio)

