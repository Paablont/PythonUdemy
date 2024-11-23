import random

diccionario_edades = {
    "Carlos": 55,
    "María": 42,
    "Mabel": 78,
    "José": 44,
    "Lucas": 24,
    "Rocío": 35,
    "Sebastián": 19,
    "Catalina": 2,
    "Darío": 49
}

# Obtener el mínimo valor del diccionario
edad_minima = min(diccionario_edades.values())

# Obtener el último nombre en orden alfabético
ultimo_nombre = max(diccionario_edades.keys())

# Imprimir los resultados
print("Edad mínima:", edad_minima)  # Salida: 2
print("Último nombre en orden alfabético:", ultimo_nombre)  # Salida: Sebastiá

valores = [10, 2, 8, 6, 4]
print(valores.index(min(valores)))  # Índice del mínimo: 1
print(valores.index(max(valores)))  # Índice del máximo: 0


print(random.random())  # Salida: Un número decimal entre 0 y 1
print(random.randint(1, 10))  # Entero entre 1 y 10
print(random.uniform(1, 10))  # Decimal entre 1 y 10
colores = ['rojo', 'azul', 'verde', 'amarillo']
print(random.choice(colores))  # Salida: Un color aleatorio
print(random.sample(colores, 2))  # Salida: Dos colores aleatorios (sin reemplazo)
numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)
print(numeros)  # Lista mezclada

