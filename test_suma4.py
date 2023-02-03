import unittest
import suma
from nose2.tools import params

class TestSum4(unittest.TestCase):

    def test_list_frac(self):
        """
        Test que envia una lista de fracciones y espera un entero
        """
        data=[1/1, 2/2, 3/3]
        result=sum(data)
        self.assertEqual(result,3)


    def test_list_frac2(self):
        """
        Test que envia una lista de fracciones y espera un entero
        """
        data=[1, 1/2]
        result=sum(data)
        self.assertEqual(result, 1.5)
   

    def test_list_frac3(self):
        """
        Test que envia una lista de fracciones y espera un entero
        """
        data=[-5, 4]
        result=sum(data)
        self.assertEqual(result, -1)


#    def test_list_frac_e(self):
#       """
#        Test que envia una lista de fracciones y espera un entero
#        """
#        data=[1/1, 2/2, 3/3]
#        result=sum(data)
#        self.assertEqual(result,5)

    
if __name__=="__main__":
    unittest.main()