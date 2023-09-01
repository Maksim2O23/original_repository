import unittest
from utils.arrs import get, my_slice

class TestArrsFunctions(unittest.TestCase):

    def test_get_existing_index(self):
        result = get([1, 2, 3, 4], 2, "default_value")
        self.assertEqual(result, 3)

    def test_get_non_existing_index(self):
        result = get([1, 2, 3, 4], 10, "default_value")
        self.assertEqual(result, "default_value")

    def test_get_negative_index(self):
        result = get([1, 2, 3, 4], -1, "default_value")
        self.assertEqual(result, "default_value")

    def test_my_slice_with_start(self):
        result = my_slice([1, 2, 3, 4], 1)
        self.assertEqual(result, [2, 3, 4])

    def test_my_slice_with_end(self):
        result = my_slice([1, 2, 3, 4], end=3)
        self.assertEqual(result, [1, 2, 3])

    def test_my_slice_with_negative_indices(self):
        result = my_slice([1, 2, 3, 4], -2, -1)
        self.assertEqual(result, [3])

    def test_my_slice_with_out_of_range_indices(self):
        result = my_slice([1, 2, 3, 4], 10, 20)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
