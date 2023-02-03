import unittest
from my_sum import my_sum_1
from nose2.tools import params


class TestSum3(unittest.TestCase):
    def test_list_int(self):
        """
        Test que retorna la suma de una lista de enteros
        """
        data=[1,2,3]
        result=my_sum_1(data)
        self.assertEqual(result,6)
    
    @params(([1,2,3],6))
    def test_example_params(self,lista,resultado):
        self.assertEqual(my_sum_1(lista),resultado)
    
