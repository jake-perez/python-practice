import unittest
from fib import fib_slow


class FibonacciTests(unittest.TestCase):
    def test_fib_slow(self):
        self.assertEqual(fib_slow(4), 5, '4th fibonaccis number is 5')

    def test_fib_slow_value_error(self):
        self.assertRaises(ValueError, fib_slow, -2)


if __name__ == '__main__':
    unittest.main()
