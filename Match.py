#Basicamente el switch

serie = 'N-02'

match serie:
    case 'N-01':
        print('Samgsumg')
    case 'N-02':
        print('Huawei')
    case 'N-03':
        print('Nokia')
    case _: #este es el default de java
        print('Ninguna marca')

#un match bastante bueno

cliente = {'nombre':'Pablo',
           'edad':23,
           'trabajo':'informatico'}
pelicula = {'titulo':'Spiderman',
            'ficha_tecnica':{'protagonista':'Tobey Maguire',
                             'director':'Sam Raimi'}}

combinados = [cliente,pelicula,'libro']

for e in combinados: #Va recorriendo combinados y segun loq ue sea cada objeto pues hace un case u otro
    match e:
        case {'nombre':nombre,
           'edad':edad,
           'trabajo':trabajo}:
            print('Es un cliente')
            print(nombre, edad, trabajo)
        case {'titulo':titulo,
              'ficha_tecnica':{'protagonista':protagonista,
                               'director':director}}:
            print('Es una pelicula')

        case _:
            print('No existe en la BBDD')