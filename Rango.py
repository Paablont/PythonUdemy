lista = [1,2,3,4]

for i in lista:
    print(i)

print('Con rango 4')
#usando rango, podemos definir cuanto queremos que recorra (no incluye el último)
for i in range(4):
    print(i)
print('Con rango desde 1 a 4')
for i in range(2,4):
    print(i)
print('Con rangos del 20 al 30')
for i in range(20,30):
    print(i)

print('Con rangos del 20 al 30 cada 2 numeros')
for i in range(20,30,2):
    print(i)

#imagina que queremos una lista del 1 al 100. Mas facil con range
lista_rangos = list(range(1,101))
for i in lista_rangos:
    print(i)