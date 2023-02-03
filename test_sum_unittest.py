import unittest

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1,2,3]),6,"Debería ser 6!")
    
    def test_sum_tuple(self):
        self.assertEqual(sum((1,2,3)),6,"Debería ser 6!")

    def test_sum_tuple2(self):
        self.assertFalse(sum((1,2,2))==6)

    
if __name__=="__main__":
    unittest.main()