from turtle import Vec2D
import unittest
from webbrowser import Opera
import Operaciones

class test_Operaciones(unittest.TestCase):

    def test_suma_valido(self):
        #arrange test
        v1 = 10
        v2 = 10
        res_esperado = 20
        res_actual = 0

        #act
        operaciones = Operaciones.Operaciones()
        res_actual = operaciones.suma(v1,v2)
        
        

        antinone = "" 
        if res_actual < res_esperado:
            antinone ="El resultado esperado es menor que el ingresado: {}".format(res_actual)
            
        elif res_actual > res_esperado:
            antinone ="El resultado esperado es mayor que el ingresado:{}".format(res_actual)
            
        else :
            antinone ="El resultado esta correcto y es:{}".format(res_actual)
        
        return antinone   
        #assert
        self.assertEqual(res_actual, res_esperado)

    def test_resta_valido(self):
        v1 = 1
        v2 = 2 
        res_esperado = 1
        res_actual = 0

        operaciones = Operaciones.Operaciones()
        res_actual = operaciones.resta(v1,v2)

        self.assertEqual(res_actual,res_esperado)
        
    def test_multiplicacion_valido(self):
        v1 = 10
        v2 = 10
        res_esperado = 4
        res_actual = 0

        operaciones = Operaciones.Operaciones()
        res_actual = operaciones.multiplicacion(v1,v2)

        self.assertEqual(res_actual,res_esperado)

    def test_division_valido(self):
        v1 = 10
        v2 = 10
        res_esperado = 2
        res_actual = 0

        operaciones = Operaciones.Operaciones()
        res_actual = operaciones.division(v1,v2)

        self.assertEqual(res_actual,res_esperado)

    
    def test_potencia_valido(self):
        v1 = 10
        v2 = 10
        res_esperado = 25
        res_actual = 0

        operaciones = Operaciones.Operaciones()
        res_actual = operaciones.multiplicacion(v1,v2)

        self.assertEqual(res_actual,res_esperado)
        
        
        
test = test_Operaciones();
print(test.test_suma_valido())

