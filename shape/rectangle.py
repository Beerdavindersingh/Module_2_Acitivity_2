"""This module defines the Rectangle class."""

__author__ = "Beerdavinder Singh"
__version__ = ""

from shape.shape import Shape
import math

class Rectangle(Shape):
    """
    The Rectangle class represents a rectangle shape.
    """
    def _init_(self, color: str, length:int, width:int):
        """
        Args:
            color (str): The color of the rectangle.
            length (int): The length of the rectangle.
            width (int): The width of the rectangle.
        
        Raises:
            ValueError: If length or width is not a number.
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
        Returns a string.
        """
        value = super()._str_()
        value+= f"\nThis rectangle has four sides with the lengths of {self._length}, {self._width}, {self._length} and {self._width} centimeters."
        return value
    
    def calculate_area(self) -> float:
        """
        Calculates the area of the rectangle.
        """
        return self._length * self._width
    
    def calculate_perimeter(self) -> float:
        """
        Calculates the perimeter of the rectangle.
        """
        return 2 * self._length + 2 * self._width