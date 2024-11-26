texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
# Para eliminar todos loos caracteres inciiales, se pone en el () menos el caracter que no queremos eliminar (en este caso la P para que escriba el resto
texto_limpio = texto.lstrip(",:_#%")
print(texto_limpio)

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3,'naranja')

print(frutas)


marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

#Devuelve True si no hay ningún elemento en común entre los dos conjuntos.
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)
