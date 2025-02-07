"""This module defines the Shape class."""

__author__ = "Beerdavinder Singh"
__version__ = ""

from abc import ABC, abstractmethod

class shape(ABC):
    """
    A class for shapes.
    """
    def _init_(self, color: str):
        """
        Args:
        color (str): The color of the shape.
        Raises:
        ValueError: If the color is an empty.
        """
        if len(color.strip()) == 0:
            raise ValueError("Color cannot be blank")
        self._color = color.strip()

    def _str_(self) -> str:
        """
        Returns with the shape's color.
        """
        return f"The shape color is {self._color}."
    
    @abstractmethod
    def calcualte_area(self) -> float:
        """
        This method is defined to calculate its area.
        """
        pass

    @abstractmethod
    def calculate_perimeter(Self) -> float:
        """
        This method is defined to calculate its perimeter.
        """
        pass