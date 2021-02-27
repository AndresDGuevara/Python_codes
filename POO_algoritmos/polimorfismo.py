# class Persona:
#     def __init__(self, nombre):
#         self.nombre = nombre
#     @property
#     def getNombre(self):
#         return self.nombre
#     def avanza(self):
#         print(' está caminando')
    
# class Ciclista(Persona):
#     def __init__(self, nombre):
#         super().__init__(nombre)
#     def avanza (self):
#         print(' está moviéndose en bicicleta')

# def main():
#     persona = Persona('David')
#     print(f'{persona.getNombre}:') 
#     persona.avanza()

#     ciclista = Ciclista('Eugenia')
#     print(f'{ciclista.getNombre}:') 
#     ciclista.avanza()

# if __name__ == '__main__':
#     main()



class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def avanza(self):
        return 'está caminando'
    
class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def avanza (self):
        return 'está moviéndose en bicicleta'

def main():
    persona = Persona('David')
    print(f'{persona.nombre}: {persona.avanza()}')
    
    ciclista = Ciclista('Pola')
    print(f'{ciclista.nombre}: {ciclista.avanza()}') 
    

if __name__ == '__main__':
    main()