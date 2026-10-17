"""Unit tests for Polynomial. Run: python -m unittest -v test_polynomial.py"""

import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from Polynomial import Polynomial


class TestPolynomial(unittest.TestCase):
    def test_default_and_normalized_coefficients(self):
        self.assertEqual(Polynomial().coefficients, (0.0,))
        self.assertEqual(Polynomial(1, 2, 0, 0).coefficients, (1.0, 2.0))
        self.assertEqual(Polynomial(0, 0).coefficients, (0.0,))
        self.assertEqual(Polynomial(0, 0).degree, 0)

    def test_validation_methods(self):
        polynomial = Polynomial(1)
        self.assertTrue(polynomial.is_valid_coefficient(2.5))
        self.assertFalse(polynomial.is_valid_coefficient(True))
        self.assertFalse(polynomial.is_valid_coefficient("2"))
        self.assertFalse(polynomial.is_valid_coefficient(float("inf")))
        self.assertTrue(polynomial.is_valid_polynomial(Polynomial(1, 2)))
        self.assertFalse(polynomial.is_valid_polynomial("not a polynomial"))

    def test_invalid_coefficients(self):
        with self.assertRaises(TypeError):
            Polynomial("2")
        with self.assertRaises(TypeError):
            Polynomial(True)
        with self.assertRaises(ValueError):
            Polynomial(float("nan"))

    def test_degree_and_zero_detection(self):
        self.assertEqual(Polynomial(1, 2, 3).degree, 2)
        self.assertTrue(Polynomial(0, 0).is_zero())
        self.assertFalse(Polynomial(0, 1).is_zero())

    def test_coefficient_indexing(self):
        polynomial = Polynomial(1, 2, 3)
        self.assertEqual(polynomial[0], 1.0)
        self.assertEqual(polynomial[1], 2.0)
        self.assertEqual(polynomial[10], 0.0)
        with self.assertRaises(IndexError):
            _ = polynomial[-1]
        with self.assertRaises(TypeError):
            _ = polynomial[1.5]

    def test_evaluation(self):
        # Polynomial is 1 + 2x + 3x^2; at x=2 the value is 17.
        self.assertEqual(Polynomial(1, 2, 3).evaluate(2), 17.0)

    def test_addition_and_subtraction(self):
        first = Polynomial(1, 2)
        second = Polynomial(3, 1)
        self.assertEqual(first + second, Polynomial(4, 3))
        self.assertEqual(first - second, Polynomial(-2, 1))

    def test_polynomial_multiplication(self):
        self.assertEqual(Polynomial(1, 2) * Polynomial(3, 1), Polynomial(3, 7, 2))

    def test_scalar_multiplication_and_negation(self):
        polynomial = Polynomial(1, 2)
        self.assertEqual(polynomial * 2, Polynomial(2, 4))
        self.assertEqual(2 * polynomial, Polynomial(2, 4))
        self.assertEqual(-polynomial, Polynomial(-1, -2))

    def test_scalar_division(self):
        self.assertEqual(Polynomial(2, 4, 6) / 2, Polynomial(1, 2, 3))
        with self.assertRaises(ZeroDivisionError):
            _ = Polynomial(1) / 0

    def test_polynomial_division(self):
        dividend = Polynomial(-1, 0, 1)  # x^2 - 1
        divisor = Polynomial(-1, 1)       # x - 1
        self.assertEqual(dividend / divisor, Polynomial(1, 1))

    def test_polynomial_division_errors(self):
        with self.assertRaises(ZeroDivisionError):
            _ = Polynomial(1, 2) / Polynomial(0)
        with self.assertRaises(ValueError):
            _ = Polynomial(1, 0, 1) / Polynomial(1, 1)

    def test_copy_creates_separate_object(self):
        original = Polynomial(1, 2, 3)
        copied = original.copy()
        self.assertEqual(copied, original)
        self.assertIsNot(copied, original)

    def test_string_conversion_and_factory(self):
        polynomial = Polynomial(1, 2, 3)
        self.assertEqual(str(polynomial), "[1, 2, 3]")
        self.assertEqual(Polynomial.from_string("[1, 2, 3]"), polynomial)
        self.assertEqual(Polynomial.from_string(""), Polynomial(0))
        with self.assertRaises(ValueError):
            Polynomial.from_string("1, invalid")
        with self.assertRaises(TypeError):
            Polynomial.from_string(123)

    def test_repr_can_recreate_object(self):
        polynomial = Polynomial(1, 2, 3)
        recreated = eval(repr(polynomial), {"Polynomial": Polynomial})
        self.assertEqual(recreated, polynomial)


if __name__ == "__main__":
    unittest.main()
