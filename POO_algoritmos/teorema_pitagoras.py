class Teorema_pitagoras(object):

    """Esta clase hace uso del teorema de pitagoras para calcular
     la hipotenusa alrededor de difererentes catetos"""

    def __init__(self, cateto_1, cateto_2):
        self.cateto_1 = cateto_1
        self.cateto_2 = cateto_2

    def calculo_hipotenusa(self):
        hipotenusa = ((self.cateto_1 ** 2) + (self.cateto_2 ** 2)) ** 0.5
        return hipotenusa

if __name__ == '__main__':

    cateto = int(input('¿Cual es el valor del cateto 1?: '))
    cateto_2 = int(input('¿Cual es el valor del cateto 2?: '))
    resultado_1 = Teorema_pitagoras(cateto, cateto_2)

    print('El valor de la hipotenusa es ', resultado_1.calculo_hipotenusa())