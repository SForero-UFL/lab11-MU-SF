import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self): # 3 assertions
            self.assertEqual(add(5, 5), 10)
            self.assertEqual(add(0, 5), 5)
            self.assertEqual(add(-10, 9), 1)

    def test_subtract(self):  # 3 assertions
            self.assertEqual(subtract(10, 5), 5)
            self.assertEqual(subtract(-28, 6), -34)
            self.assertEqual(subtract(10, -6), 16)

    def test_divide_by_zero(self):  # 1 assertion
            with self.assertRaises(ZeroDivisionError):
                div(0, 5)



    def test_logarithm(self):  # 3 assertions
            self.assertEqual(logarithm(4, 64), 3)
            self.assertEqual(logarithm(2, 32), 5)
            self.assertEqual(logarithm(2, 64), 6)

    def test_log_invalid_base(self):  # 1 assertion
            with self.assertRaises(ValueError):
                log(-1, 0)


# Do not touch this
if __name__ == "__main__":
    unittest.main()