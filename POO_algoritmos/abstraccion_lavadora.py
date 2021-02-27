class Lavadora:
  def __init__(self):
    pass
  def lavar(self, temperatura = 'caliente'):
    #internamente llamando metodos privados que al usuario no le
    # interesan 
    self._llenar_tanque_de_agua(temperatura)
    self._añadir_jabon()
    self._lavar()
    self._centrifugar()

  def _llenar_tanque_de_agua(self, temperatura):
    print(f'llenando el tanque de agua {temperatura}')
  
  def _añadir_jabon(self):
    print('añadiendo jabon')
  
  def _lavar(self): #guion bajo es un metodo privado
    print('Lavando la ropa')
  
  def _centrifugar(self):
    print('Centrifugando la ropa')

if __name__ == '__main__':
  lavadora = Lavadora()
  lavadora.lavar()

# La abstraccion es el movimiento, las herramientas que se utilizan 
# para medir todo lo que se hace en la vida.