class Coordenada:
    def __init__(self, x, y): # Metodo __init__ es el constructor
        # Variales
        self.x = x 
        self.y = y

    def distancia(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x) ** 2 # Diferencia de x
        y_diff = (self.y - otra_coordenada.y) ** 2 # Diferencia de y

        return(x_diff + y_diff) ** 0.5 # Elevar a  la raiz cuadrada con 0.5,
                                       #se obtiene la raiz cuadrada de las diferencia al cuadrado

if __name__ == '__main__': # Si este programa se ejecuta desde la terminal lo podemos correr
    coord_1 = Coordenada(3, 30) # Instancia de la primera coordenada
    coord_2 = Coordenada(4, 8) # Instancia de la segunda coordenada

    # print(coord_1.distancia(coord_2)) # Saber la distancia 1 y pasamos como segundo parametro la coordenada 2
    # print(isinstance(coord_2, Coordenada)) # Instancia True
    print(isinstance(3, Coordenada)) # Instancia False

    # Primero tenemos un molde llamado Coordenada
    # De estas Coordenadas podemos generar dos instancias coord_1 y coord_2
    # Podemos ejecutar directamnete los metodos que nosotros definamos adentro de esta clase

    # Generando clases para generar muchas instancias
    # Determinar si una instancia pertenece a una clase
    # Utilizar directamnete los metodos de la clase

    # "Mientras que la clase es un molde, los objetos creados se les conoce como instancias"
    # David Arosesti de Platzy
