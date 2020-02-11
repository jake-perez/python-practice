import unittest
from rgb_sort import rgb_sort


class RGBTests(unittest.TestCase):
    def test_rgb_sort(self):
        arr = ['G', 'R', 'B', 'G', 'B', 'G']
        rgb_sort(arr)
        self.assertEqual(arr, ['R', 'G', 'G', 'G', 'B', 'B'])


if __name__ == "__main__":
    unittest.main()
