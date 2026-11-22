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




    def test_multiply(self):
        self.assertEqual(multiply(2, 4), 8)
        self.assertEqual(multiply(-3, 2), -6)
        self.assertEqual(multiply(0, 2), 0)



    def test_divide(self):
        self.assertEqual(divide(2, 4), 2)
        self.assertAlmostEqual(divide(3, 1), 0.3333333)
        self.assertRaises(ZeroDivisionError, divide, 0, 4)



    def test_logarithm(self):  # 3 assertions
            self.assertEqual(logarithm(4, 64), 3)
            self.assertEqual(logarithm(2, 32), 5)
            self.assertEqual(logarithm(2, 64), 6)


    def test_log_invalid_base(self):  # 1 assertion
            with self.assertRaises(ValueError):
                log(-1, 0)



    def test_log_invalid_argument(self):
        self.assertRaises(ValueError, logarithm, 0, 5)


    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(-3, -4), 5)
        self.assertAlmostEqual(hypotenuse(3, 2), 3.6055512)

    def test_sqrt(self):
        self.assertEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(3), 1.73205080757)
        self.assertRaises(ValueError, square_root, -1)

# Do not touch this
if __name__ == "__main__":
    unittest.main()