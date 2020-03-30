from math import pi
from unittest import TestCase, main
from unittest.mock import patch

import shape


class Test(TestCase):
    def test_rectangle(self):
        self.assertEqual(shape.get_rectangle_properties(1, 1), (1, 4))
        self.assertEqual(shape.get_rectangle_properties(1, 2), (2, 6))
        self.assertEqual(shape.get_rectangle_properties(1, 3), (3, 8))
        self.assertEqual(shape.get_rectangle_properties(3, 3), (9, 12))
        self.assertEqual(shape.get_rectangle_properties(12, 20), (240, 64))
        self.assertEqual(shape.get_rectangle_properties(12, 20), (240, 64))
        with self.assertRaises(ValueError):
            shape.get_rectangle_properties(0, 1)
        with self.assertRaises(ValueError):
            shape.get_rectangle_properties(1, 0)
        with self.assertRaises(ValueError):
            shape.get_rectangle_properties(-1, 1)
        with self.assertRaises(ValueError):
            shape.get_rectangle_properties(1, -1)
        with self.assertRaises(ValueError):
            shape.get_rectangle_properties(0, 0)

    def test_circle(self):
        self.assertEqual(shape.get_circle_properties(1), (pi, 2*pi))
        self.assertEqual(shape.get_circle_properties(2), (4*pi, 4*pi))
        self.assertEqual(shape.get_circle_properties(3), (9*pi, 6*pi))
        self.assertEqual(shape.get_circle_properties(12), (144*pi, 24*pi))
        self.assertEqual(shape.get_circle_properties(20), (400*pi, 40*pi))
        with self.assertRaises(ValueError):
            shape.get_circle_properties(0)
        with self.assertRaises(ValueError):
            shape.get_circle_properties(-1)


if __name__ == '__main__':
    main()
