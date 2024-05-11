import math
import unittest
from area import calculate_area

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        radius = 7
        expected_area = math.pi * (radius ** 2)
        self.assertEqual(calculate_area(radius), expected_area)
        
if __name__ == '__main__':
    unittest.main()