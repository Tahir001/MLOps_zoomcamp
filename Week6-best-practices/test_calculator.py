import unittest
from calculator import add, subtract, multiply, divide, integer_divide, power, square_root

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2,5), 7)
        self.assertEqual(add(2,10),12)
        self.assertNotEqual(add(2,10),15)

    def test_subtract(self):
        self.assertEqual(subtract(2,6), -4)
        self.assertEqual(subtract(10,5), 5)
        self.assertEqual(subtract(-1,-1), 0)
    
    def test_multiply(self):
        self.assertEqual(multiply(2,2), 4)
        self.assertEqual(multiply(2,10),20)
    
    def test_divide(self):
        self.assertEqual(divide(10,2), 5.0)
    
    def test_integer_divide(self):
        self.assertEqual(integer_divide(10,2), 5)
    
    def test_power(self):
        self.assertEqual(power(2,3), 8)
    
    def test_square_root(self):
        self.assertEqual(square_root(4),2)

if __name__ == '__main__':
    unittest.main()