import unittest
import multiply

class TestMultiplyInt(unittest.TestCase):

    def test_multiplyints(self):
        self.assertEqual(multiply.multiply(0,0),"0")
        self.assertEqual(multiply.multiply(1,1),"1")
        self.assertEqual(multiply.multiply(10,10),"100")
        self.assertEqual(multiply.multiply(10,2),"20")
        self.assertEqual(multiply.multiply(31,59),"1829")
        

if __name__ == '__main__':
    unittest.main()