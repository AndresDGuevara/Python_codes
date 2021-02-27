# Atributos de Instancia
class hotel:
    def __init__(self, maximo_de_huespedes, estacionamientos):
        self.maximo_de_huespedes = maximo_de_huespedes
        self.estacionamientos = estacionamientos
        self.huespedes = 0
        self.vehiculos = 0

    def añadir_huespedes(self, huespedes):
        self.huespedes +=  huespedes

    def checkout(self, huespedes):
        self.huespedes -=  huespedes
    
    def ocupacion_total(self):
        return self.huespedes
        
class parking(hotel): 

    def __init__(self, maximo_de_huespedes, estacionamientos):
        super().__init__(estacionamientos)       
    
    def añadir_vehiculos(self, vehiculos):
        self.vehiculos += vehiculos

    def salida_vehiculos(self, vehiculos):
        self.vehiculos -= vehiculos
    
    def parcking_disponible(self):
        return self.vehiculos
        

dante_hotel = hotel(50, 20)

def main():
    print(f'Numero maximo de huespedes es {dante_hotel.maximo_de_huespedes}')
    print(f'Numero maximo de estacionamientos es {dante_hotel.estacionamientos}')

    añadir = int(input("Añadir numero de huespedes: ")) 
    dante_hotel.añadir_huespedes(añadir)

    carro = parcking int(input("Numero de vehiculos: "))
    dante_hotel.añadir_vehiculos(carro)

    salida = int(input("Numero de huespedes que salen: "))
    dante_hotel.checkout(salida)

    salida_2 = int(input("Numero de vehiculos que salen: "))
    dante_hotel.salida_vehiculos(salida_2)

    print(f'La Ocupacion de huespedes es: {dante_hotel.ocupacion_total()}')
    print(f'La ocupacion de parking es: {dante_hotel.parcking_disponible}') #Buscar solucion a este print con sus funciones


if __name__ == '__main__':
    main()
    
    