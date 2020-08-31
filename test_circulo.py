import unittest

from circulo import area_circulo
from math import pi

class TestAreaCirculo(unittest.TestCase):
    def test_area(self):
        #Prueba de Area cuando radio >=0
        self.assertAlmostEqual(area_circulo(1), pi)
        self.assertAlmostEqual(area_circulo(0), 0)
        self.assertAlmostEqual(area_circulo(2.1), pi * 2.1**2)
    
    def test_values(self):
        #Asegúrese de que se generen errores de valor cuando sea necesario
        self.assertRaises(ValueError, area_circulo, -2)

    def test_tipos(self):
        #Asegúrese de que se generen errores de valor cuando sea necesario
        self.assertRaises(TypeError, area_circulo, 3+5j)
        self.assertRaises(TypeError, area_circulo, True)
        self.assertRaises(TypeError, area_circulo, "radio")