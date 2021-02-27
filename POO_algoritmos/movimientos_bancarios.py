class movimientos:
    def __init__ (self, nombre):
        self.saldo = 0
        self.propietario = nombre

    def deposito (self, cantidad):
        self.saldo = self.saldo + cantidad
        return self.saldo

    def retiro (self, cantidad):
        if cantidad > self.saldo:
            return ('fondos insuficiente')
        self.saldo = self.saldo - cantidad
        return (self.saldo)


if __name__ == '__main__':

    cc = movimientos (str(input('Escribe tu nombre: ')))

    print(f'Tu saldo actual es {cc.saldo}')

    cc.deposito(int(input('Escribe el valor a depositar: ')))

    print(f'Tu saldo actual es {cc.saldo}')
    
    cc.retiro(int(input('Escribe el valor a retirar: ')))
    

    # if cc.saldo <= 0:
    #     print (f'{cc.propietario} Tu saldo actual disponible es: {cc.saldo}')

    # else:
    #     print('Fondos insuficientes')
    
    #Hay que corregir el ultimo if 