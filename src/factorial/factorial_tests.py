import unittest
import factorial


class FactorialTests(unittest.TestCase):
    def test_factorial_zero(self):
        self.assertEqual(factorial.factorial_recursive(0), 1, '0! == 1')

    def test_factorial_negative(self):
        self.assertRaises(ValueError, factorial.factorial_recursive, -1)


if __name__ == '__main__':
    unittest.main()
