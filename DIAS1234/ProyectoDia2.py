# La situación es esta: tú trabajas en una empresa donde los vendedores reciben comisiones
# del 13% por sus ventas totales, y tu jefe quiere que ayudes a los vendedores a calcular sus
# comisiones creando un programa que les pregunte su nombre y cuánto han vendido en este
# mes. Tu programa le va a responder con una frase que incluya su nombre y el monto que le
# corresponde por las comisiones

comision = 0.13

nombre = input('Bienvenido al calculador de salario. Por favor escribe tu nombre ')
total_vendido = int(input(f'Bienvenido {nombre}, indica cuanto has vendido en este mes (en euros): '))

#Tambien podria crear una variable nueva y hacer el int, pero soy un pro xd
salario = round(float(total_vendido * comision),2)

print(f'Este mes has vendido {total_vendido}. Tu salario es de: {salario} €. Felicidades!')