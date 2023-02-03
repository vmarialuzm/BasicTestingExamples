import unittest

class Hola:
    msg:str

    def __init__(self,msg):
        self.msg=msg

def raise_if_negative(value):
    if value < 0:
        raise ValueError("El valor no puede ser negativo!")

def divider():
    raise ZeroDivisionError

class TestSum5(unittest.TestCase):

    def test_assert1(self):
        lista=[1,2,3,4,5,6,7,8,9]
        self.assertIn(5,lista)
        

    def test_assert2(self):
        lista=[1,2,3,4,5,6,7,8,9]
        self.assertNotIn(15,lista)


    def test_assert3(self):
        self.assertAlmostEqual(1.10, 1.11, delta=0.1)

    
    def test_assert4(self):
        self.assertNotAlmostEqual(1.1234567,1.1234568)


    def test_assert5(self):
        self.assertNotEqual(1,2)

    
    def test_assert6(self):
        lista=[1,2,3,4,5]
        self.assertIsInstance(lista,list)

    
    def test_assert7(self):
        inst_hola=Hola("Hola")
        self.assertIsInstance(inst_hola,Hola)


    def test_assert8(self):
        with self.assertRaises(ValueError):
            raise_if_negative(-1)


    def test_assert9(self):
        with self.assertRaises(ZeroDivisionError):
            divider()


if __name__=="__main__":
    unittest.main()