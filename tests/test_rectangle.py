"""This module defines the TestRectangle class.

Usage: 
    To execute all tests in the terminal execute the following command:

    $ python -m unittest tests/test_rectangle.py
"""

__author__ = ""
__version__ = ""

import unittest
import math
from shape.rectangle import Rectangle

class rectangletests(unittest.TestCase):
    """
    """
    def setup(self):
        """
        """
        self.rectangle = Rectangle("grey", 7, 8)

    def test_blank_color(self):
        """
        """
        with self.assertRaises(ValueError):
            self.rectangle = Rectangle("", 7, 8)

    def test_length_not_integar(self):
        """
        """
        with self.assertRaises(ValueError):
            self.rectangle = Rectangle("grey", "bs", 8)

    def test_width_not_integar(self):
        """
        """
        with self.assertRaises(ValueError):
            self.rectangle = Rectangle("grey", 7, "bs")

    def test_str_(self):
        """
        """
        self.rectangle = Rectangle("grey", 7, 8)
        expected_str = "The shape color is grey.\nThis rectangle has four sides with the lengths of 7, 8, 7 and 8 centimeters."      
        self.assertEqual(str(self.rectangle), expected_str)

    def test_calculate_area(self):
        """
        """
        self.rectangle = Rectangle("grey", 7, 8)
        expected_area = 7 * 8 
        self.assertEqual(self.rectangle.calculate_area(), expected_area)

    def test_calculate_perimeter(self):
        """
        """
        self.rectangle = Rectangle("grey", 7, 8)
        expected_perimeter = 7 * 2 + 8 * 2
        self.assertEqual(self.rectangle.calculate_perimeter(), expected_perimeter)
