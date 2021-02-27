class Rectangulo: # Super Clase

    def __init__(self, base, altura): # metodo que calcula el area
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Cuadrado(Rectangulo): # la clase cuadrado extiende al rectangulo

    def __init__(self, lado):
        super().__init__(lado, lado) # llamamos a la Super Clase


if __name__ == '__main__':
    rectangulo = Rectangulo(base=3, altura=4)
    print(rectangulo.area())

    cuadrado = Cuadrado(lado=5)
    print(cuadrado.area())