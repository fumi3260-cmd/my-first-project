"""test_calculator.py — Calculator クラスのユニットテスト（unittest）"""

import unittest
from calculator import Calculator


class TestAdd(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_integers(self):
        self.assertEqual(self.calc.add(3, 4), 7)

    def test_add_floats(self):
        self.assertAlmostEqual(self.calc.add(1.5, 2.5), 4.0)

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-3, -7), -10)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5)


class TestSubtract(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_subtract_integers(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(-5, -3), -2)

    def test_subtract_zero(self):
        self.assertEqual(self.calc.subtract(7, 0), 7)


class TestMultiply(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_multiply_integers(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(100, 0), 0)

    def test_multiply_negative(self):
        self.assertEqual(self.calc.multiply(-3, 4), -12)

    def test_multiply_floats(self):
        self.assertAlmostEqual(self.calc.multiply(2.5, 4), 10.0)


class TestDivide(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_divide_integers(self):
        self.assertEqual(self.calc.divide(10, 2), 5.0)

    def test_divide_floats(self):
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0)

    def test_divide_negative(self):
        self.assertEqual(self.calc.divide(-9, 3), -3.0)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ValueError) as ctx:
            self.calc.divide(10, 0)
        self.assertIn("0で割ることはできません", str(ctx.exception))

    def test_divide_by_zero_float_raises(self):
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0.0)


if __name__ == "__main__":
    unittest.main()
