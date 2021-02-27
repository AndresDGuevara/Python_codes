class Automovil:
  def __init__(self, modelo, marca, color):
    self.modelo = modelo
    self.marca = marca
    self.color = color
    self._estado = 'en reposo' # el guin bajo _ indica que es una variable privada
    self._motor = Motor(cilindros = 12) # variable privada

  def acelelar(self, tipo = 'despacio'):
    if tipo == 'rapida':
      self._motor.inyecta_gasolina(10)
    else:
      self._motor.inyecta_gasolina(3)
    self._estado = 'en_movimiento'

class Motor:
  def __init__(self, cilindros, tipo = 'gasolina'): #defaut keyword tipo=gasolina
    self.cilindros = cilindros
    self.tipo = tipo
    self._temperatura = 0

  def inyecta_gasolina(self, cantidad): 
    pass


if __name__ == '__main__':
    carro = Automovil('RSQ8', 'Audi', 'Rojo')
    carro.acelelar('rapida')
    
