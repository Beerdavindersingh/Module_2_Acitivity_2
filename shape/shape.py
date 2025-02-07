"""This module defines the Shape class."""

__author__ = "Beerdavinder Singh"
__version__ = ""

from abc import ABC, abstractmethod

class shape(ABC):
    def _init_(self, color: str):
        if len(color.strip()) == 0:
            raise ValueError("Color cannot be blank")
        self._color = color.strip()

    def _str_(self) -> str:
        return f"The shape color is {self._color}."
    
    @abstractmethod
    def calcualte_area(self) -> float:
        pass

    @abstractmethod
    def calculate_perimeter(Self) -> float:
        pass