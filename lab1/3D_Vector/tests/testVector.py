"""Unit tests for Vector3D."""
import unittest
import sys
import os

# This tells Python to look in the folder ABOVE 'tests' (which is 3D_Vector)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.Vector import Vector3D


class TestVector3D(unittest.TestCase):
    def test_default_values_and_properties(self):
        vector = Vector3D()
        self.assertEqual(vector.coordinates, (0.0, 0.0, 0.0))
        self.assertEqual((vector.x, vector.y, vector.z), (0.0, 0.0, 0.0))

    def test_validation_methods(self):
        vector = Vector3D()
        self.assertTrue(vector.is_valid_coordinate(2.5))
        self.assertFalse(vector.is_valid_coordinate(True))
        self.assertFalse(vector.is_valid_coordinate("2"))
        self.assertFalse(vector.is_valid_coordinate(float("inf")))
        self.assertTrue(vector.is_valid_vector(Vector3D(1, 2, 3)))
        self.assertFalse(vector.is_valid_vector("not a vector"))

    def test_invalid_constructor_arguments(self):
        with self.assertRaises(TypeError):
            Vector3D("1", 2, 3)
        with self.assertRaises(TypeError):
            Vector3D(True, 2, 3)
        with self.assertRaises(ValueError):
            Vector3D(float("nan"), 2, 3)

    def test_length(self):
        self.assertEqual(Vector3D(1, 2, 2).length(), 3.0)

    def test_dot_product(self):
        self.assertEqual(Vector3D(1, 2, 2).dot(Vector3D(2, 0, 1)), 4.0)

    def test_cross_product(self):
        self.assertEqual(
            Vector3D(1, 2, 2).cross(Vector3D(2, 0, 1)),
            Vector3D(2, 3, -4),
        )

    def test_cosine_between_perpendicular_vectors(self):
        result = Vector3D(1, 0, 0).cosine_with(Vector3D(0, 1, 0))
        self.assertAlmostEqual(result, 0.0)

    def test_cosine_with_zero_vector_raises_error(self):
        with self.assertRaises(ValueError):
            Vector3D().cosine_with(Vector3D(1, 0, 0))

    def test_addition_and_subtraction(self):
        first = Vector3D(1, 2, 3)
        second = Vector3D(4, 5, 6)
        self.assertEqual(first + second, Vector3D(5, 7, 9))
        self.assertEqual(first - second, Vector3D(-3, -3, -3))

    def test_in_place_addition_and_subtraction(self):
        vector = Vector3D(1, 2, 3)
        vector += Vector3D(1, 1, 1)
        self.assertEqual(vector, Vector3D(2, 3, 4))
        vector -= Vector3D(1, 1, 1)
        self.assertEqual(vector, Vector3D(1, 2, 3))

    def test_scalar_and_cross_product_operators(self):
        vector = Vector3D(1, 2, 3)
        other = Vector3D(4, 5, 6)
        self.assertEqual(vector * 2, Vector3D(2, 4, 6))
        self.assertEqual(2 * vector, Vector3D(2, 4, 6))
        self.assertEqual(vector * other, vector.cross(other))

    def test_in_place_scalar_multiplication_and_division(self):
        vector = Vector3D(2, 4, 6)
        vector *= 2
        self.assertEqual(vector, Vector3D(4, 8, 12))
        vector /= 2
        self.assertEqual(vector, Vector3D(2, 4, 6))

    def test_division_and_unary_minus(self):
        vector = Vector3D(2, 4, 6)
        self.assertEqual(vector / 2, Vector3D(1, 2, 3))
        self.assertEqual(-vector, Vector3D(-2, -4, -6))
        with self.assertRaises(ZeroDivisionError):
            vector / 0
        with self.assertRaises(TypeError):
            vector / "two"

    def test_comparisons_use_vector_length(self):
        short = Vector3D(1, 0, 0)
        long = Vector3D(0, 3, 0)
        self.assertLess(short, long)
        self.assertLessEqual(short, long)
        self.assertGreater(long, short)
        self.assertGreaterEqual(long, short)

    def test_comparison_with_non_vector_raises(self):
        with self.assertRaises(TypeError):
            _ = Vector3D(1, 0, 0) < "x"

    def test_equality_with_non_vector(self):
        self.assertNotEqual(Vector3D(1, 0, 0), "x")

    def test_copy_creates_separate_object(self):
        original = Vector3D(1, 2, 3)
        copied = original.copy()
        self.assertEqual(copied, original)
        self.assertIsNot(copied, original)

    def test_hash_is_available(self):
        vector = Vector3D(1, 2, 3)
        self.assertEqual(hash(vector), hash(vector.coordinates))
        self.assertEqual(len({vector, Vector3D(1, 2, 3)}), 1)

    def test_string_conversion_and_factory(self):
        vector = Vector3D(1, 2, 3)
        self.assertEqual(str(vector), "(1, 2, 3)")
        self.assertEqual(Vector3D.from_string("(1, 2, 3)"), vector)
        self.assertEqual(Vector3D.from_string("1, 2, 3"), vector)
        with self.assertRaises(ValueError):
            Vector3D.from_string("1, 2")
        with self.assertRaises(TypeError):
            Vector3D.from_string(123)

    def test_repr_can_recreate_object(self):
        vector = Vector3D(1, 2, 3)
        recreated = eval(repr(vector), {"Vector3D": Vector3D})
        self.assertEqual(recreated, vector)


if __name__ == "__main__":
    unittest.main()