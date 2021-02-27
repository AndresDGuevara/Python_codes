class CasillaDeVotacion:
    
    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = None

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        if region in self._pais:
            self._region = region
        else:
            raise ValueError(f'La region {region} no es valida en {self._pais}')


casilla = CasillaDeVotacion(123,['Colombia','Calarca'])
print(casilla.region)
casilla.region = 'Colombia'
print(casilla.region)

# La forma de implementar getters es con el @property
# La forma de implementar setters es con el nombre de la propiedad .setter
# tambien utilizando notacion de decorador @ y dentro de estas funciones
# podemos determinar cuando y como se puede acceder a estas variables y
# cuando y como podemos modificarlas
# esto nos da control de nuestra clase y que cambios no autorizados pudieran
# modificar nuestro algoritmo de nuestra clase

# @property = vamos a acceder a esa funcion a traves de dot notation 
# @region.setter = vamos a modificar el valor(en esta se cambia el nombre
# despues de @ dependiendo de la funcion)