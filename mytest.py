import unittest
from contador import contar_palabras
class TestContarPalabras(unittest.TestCase):
    
    def test_contar_palabras(self):
        frase = "Hola mundo, hola Python, holA america, alemania "
        resultado = contar_palabras(frase)
        self.assertEqual(resultado["Hola"], 3)
        self.assertEqual(resultado["mundo"], 1)
        self.assertEqual(resultado["hola,"], 1)
        self.assertEqual(resultado["Phyton"], 1)
        self.assertEqual(resultado["holA"], 1)
        
if __name__ == '_main_':
    unittest.main()