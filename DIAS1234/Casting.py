#Cast a string
num1 = str(123)      # Entero a string → "123"
num2 = str(45.67)    # Float a string → "45.67"
num3 = str(True)     # Booleano a string → "True"

#Cast a int float (SI EL VALOR NO ES NUMERO, DARA ERROR OBVIAMENTE
num1 = int("123")  # String a entero
num2 = int(45.67)  # Float a entero → Trunca a 45
num3 = int(True)   # Booleano a entero → 1

num1 = float("123.45")  # String a float
num2 = float(100)       # Entero a float → 100.0
num3 = float(False)     # Booleano a float → 0.0

#Cast a list
lista1 = list("Hola")       # String a lista → ['H', 'o', 'l', 'a']
lista2 = list((1, 2, 3))    # Tupla a lista → [1, 2, 3]
lista3 = list({4, 5, 6})    # Set a lista → [4, 5, 6]

#Cast a tuplas
tupla1 = tuple("Hola")      # String a tupla → ('H', 'o', 'l', 'a')
tupla2 = tuple([1, 2, 3])   # Lista a tupla → (1, 2, 3)
tupla3 = tuple({4, 5, 6})   # Set a tupla → (4, 5, 6)

#Cast a sets
set1 = set("Hola")         # String a set → {'H', 'o', 'l', 'a'}
set2 = set([1, 2, 2, 3])   # Lista a set → {1, 2, 3}
