import unittest
from simple_calculator import SimpleCalculator
class TestSimpleCalculator(unittest.TestCase):

    # Set up the SimpleCalculator instance before each test
    def setUp(self):
        self.calc = SimpleCalculator()

    # Test the addition method
    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(0, 0), 0)

    # Test the subtraction method
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    # Test the multiplication method
    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-5, -3), 15)
        self.assertEqual(self.calc.multiply(0, 0), 0)

    # Test the division method
    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertIsNone(self.calc.divide(6, 0))  # Division by zero
        self.assertEqual(self.calc.divide(0, 3), 0)
        with self.assertRaises(TypeError):
            self.calc.divide('a', 3)  # Division by non-numeric input
