import unittest
from fib import fib_slow, fib_fast


class FibonacciTests(unittest.TestCase):
    def test_fib_slow(self):
        self.assertEqual(fib_slow(25), 121393, '4th fibonaccis number is 5')

    def test_fib_slow_value_error(self):
        self.assertRaises(ValueError, fib_slow, -2)

    def test_fib_fast(self):
        self.assertEqual(fib_fast(25), 121393)


if __name__ == '__main__':
    unittest.main()
