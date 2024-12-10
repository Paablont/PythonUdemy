class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self,nombre,apellido,num_cuenta,balance):
        super().__init__(nombre,apellido)
        self.num_cuenta = num_cuenta
        self.balance = balance

    def ver_saldo(self):
        print(f'Su balance actual es: {self.balance}')

    def retirar(self,cantidad):
        if self.balance < cantidad:
            print('Lo sentimos, la cantidad a retirar no puede ser mayor al balance actual de la cuenta')
        else:
            self.balance -= cantidad
    def depositar(self,cantidad):
        self.balance += cantidad

    def __str__(self):
        return f'{self.nombre} {self.apellido}. Numero de cuenta: {self.num_cuenta}'

print('Bienvenido al Banco Python')
salir = False
cliente1 = Cliente('Pablo','Villaseñor',33212,2200)
while not salir:
    print('1. VER DATOS DE LA CUENTA')
    print('2. VER BALANCE ACTUAL')
    print('3. DEPOSITAR EN CUENTA')
    print('4 RETIRAR DE CUENTA')
    print('5. CERRAR SESION')
    opcion = int(input('Por favor, escriba la operación que desea realizar '))
    match opcion:
        case 1:
            print(cliente1)
        case 2:
            cliente1.ver_saldo()
        case 3:
            cantidad_depositar = int(input('Cuanto dinero quiere ingresar?'))
            cliente1.depositar(cantidad_depositar)
            cliente1.ver_saldo()
        case 4:
            cantidad_retirar = int(input('Cuanto dinero quiere retirar?'))
            cliente1.retirar(cantidad_retirar)
            cliente1.ver_saldo()
        case 5:
            print('Hasta pronto!')
            salir = True