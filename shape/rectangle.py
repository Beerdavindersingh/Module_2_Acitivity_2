"""This module defines the Rectangle class."""

__author__ = "Beerdavinder Singh"
__version__ = ""

from shape.shape import Shape
import math

class Rectangle(Shape):
    """
    """
    def _init_(self, color: str, length:int, width:int):
        """
        """
        super()._init_(color)
        if not isinstance(length, int):
            raise ValueError("Length must be numeric.")
        self._length = length

        if not isinstance(width,int):
            raise ValueError("Width must be numeric")
        self._width = width

    def _str_(self) -> str:
        """
        """
        value = super()._str_()
        value+= f"\nThis rectangle has four sides with the lengths of {self._length}, {self._width}, {self._length} and {self._width} centimeters."
        return value
    
    def calculate_area(self) -> float:
        """
        """
        return self._length * self._width
    
    def calculate_perimeter(self) -> float:
        """
        """
        return 2 * self._length + 2 * self._width