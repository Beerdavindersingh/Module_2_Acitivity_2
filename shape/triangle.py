"""This module defines the Triangle class."""

__author__ = "Beerdavinder Singh"
__version__ = ""

from shape.shape import Shape
import math

class Triangle(Shape):
    """
    """
    def _init_(self, color: str, side_1:int, side_2: int, side_3:int):
        """
        """
        super()._init_(color)

        if not isinstance(side_1, int):
            raise ValueError("Side 1 must be numeric")
        if not isinstance(side_2, int):
            raise ValueError("Side 2 must be numeric")
        if not isinstance(side_3, int):
            raise ValueError("Side 3 must be numeric")
        
        if not (side_1 + side_2 > side_3 and
                side_1 + side_3 > side_2 and 
                side_2 + side_3 > side_1):
            raise ValueError("The sides do not satisfy the Triangle Inequality Theorem.")
        
        self._side_1 = side_1
        self._side_2 = side_2
        self._side_3 = side_3

    def _str_(self) -> str:
        """
        """
        value = super()._str_()
        value+= f"\n This triangle has three sides with the lengths of {self._side_1}, {self._side_2}, and {self._side_3} centimeters."
        return value
    
    def calcualte_area(self) -> float:
        """
        """
        semi_perimeter = (self._side_1 + self._side_2 + self._side_3) / 2
        area = math.sqrt(semi_perimeter * (semi_perimeter - self._side_1) *
                         (semi_perimeter - self._side_2) * (semi_perimeter - self._side_3))
        return area 
    
    def calculate_perimeter(self) -> float:
        """
        """
        return (self._side_1 + self._side_2 + self._side_3)