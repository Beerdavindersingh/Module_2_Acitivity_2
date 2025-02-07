"""This module defines the TestTriangle class.

Usage: 
    To execute all tests in the terminal execute the following command:

    $ python -m unittest tests/test_triangle.py
"""

__author__ = "Beerdavinder Singh"
__version__ = ""

import unittest
import math
from shape.triangle import Triangle

class Triangletests(unittest.TestCase):
    """
    """
    def setup(self):
        """
        """
        self.triangle = Triangle("white", 7, 8, 9)

    def test_blank_color(self):
        """
        """
        with self.assertRaises(ValueError):
            self.triangle = Triangle(" ", 7, 8, 9)
    
    def test_invalid_side_1(self):
        """
        """
        with self.assertRaises(ValueError):
            self.triangle = Triangle("white", "bs", 8, 9)
        
    def test_invalid_side_2(self):
        """
        """
        with self.assertRaises(ValueError):
            self.triangle = Triangle("white", 7, "bs", 9)

    def test_invalid_side_3(self):
        """
        """
        with self.assertRaises(ValueError):
            self.triangle = Triangle("white", 7, 8,"bs")

    def test_str_format(self):
        """
        """
        self.triangle = Triangle("white", 7, 8, 9)
        expected_str = ( "The shape color is white.\nThis triangle has three sides with the lengths of 7, 8, and 9 centimeters.")
        self.assertEqual(str(self.triangle), expected_str)

    def test_calculate_area(self):
        """
        """
        self.triangle = Triangle("white", 7, 8, 9)
        perimeter = (7 + 8 + 9) / 2
        expected_area = math.sqrt(perimeter * (perimeter - 7) * (perimeter - 8) * (perimeter - 9))
        self.assertEqual(self.triangle.calculate_area(), expected_area)

    def test_calculate_perimeter(self):
        """
        """
        self.triangle = Triangle("white", 7, 8, 9)
        expected_perimeter = 7 + 8 + 9
        self.assertEqual(self.triangle.calculate_perimeter(), expected_perimeter)
