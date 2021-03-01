import unittest

# Esta funcion va en dos caminos, eres mayor de edad o no
def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

# suit de pruebas
class PuebradeCristalTest(unittest.TestCase):

    # Primer test para saber si es mayor de edad
    def test_es_mayor_de_edad(self):
        edad = 20
        # estructura de todos los test, lo preparamos, lo probamos, luego checamos que es correcto
        resultado = es_mayor_de_edad(edad)
        # Aqui verififamos que el resultado sea igual a True
        self.assertEqual(resultado, True)

    # Segundo test si es menor de edad
    def test_es_menor_de_edad(self):
        edad = 15
        resultado = es_mayor_de_edad(edad)
        self.assertEqual(resultado, False)

if __name__ == '__main__':
    unittest.main() # Correr la funcion main dentro del modulo unittest

# EAFP = Easier to Ask for Forgiveness than Permission (Python)
# LBYL = Look Before You Leap (Java)