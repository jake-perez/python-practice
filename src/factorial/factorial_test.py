import unittest
from factorial import factorial_recursive, factorial_iterative


class FactorialTests(unittest.TestCase):
    def test_factorial_zero(self):
        self.assertEqual(factorial_recursive(0), 1, '0! == 1')

    def test_factorial_negative_recursive(self):
        self.assertRaises(ValueError, factorial_recursive, -1)

    def test_factorial_recursive(self):
        self.assertEqual(factorial_recursive(4), 24, '4! = 24')

    def test_factorial_zero_iterative(self):
        self.assertEqual(factorial_iterative(0), 1, '0! = 1')


if __name__ == '__main__':
    unittest.main()
