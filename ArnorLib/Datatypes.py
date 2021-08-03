#!/usr/bin/env python
"""
Random datatypes sem ég nota oft og nenni ekki að skrifa oft
"""
__author__ = "Arnór Friðriksson"

import math
from ArnorLib import Wrappers


# 2d vector class
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"{self.__class__.__name__} ({self.x},{self.y})"

    @Wrappers.SameClass
    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __add__(self, other) -> "Vector":
        if other.__class__ == self.__class__:
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError(
                f"unsupported operand type(s) for +: '{self.__class__.__name__}' and '{other.__class__.__name__}'")

    def __sub__(self, other) -> "Vector":
        if other.__class__ == self.__class__:
            return Vector(self.x - other.x, self.y - other.y)
        else:
            raise TypeError(
                f"unsupported operand type(s) for -: '{self.__class__.__name__}' and '{other.__class__.__name__}'")

    def __mul__(self, other) -> "Vector":
        if other.__class__ == self.__class__:
            return Vector(self.x * other.x, self.y * other.y)
        elif other.__class__ == int or other.__class__ == float:
            return Vector(self.x * other, self.y * other)
        else:
            raise TypeError(
                f"unsupported operand type(s) for *: '{self.__class__.__name__}' and '{other.__class__.__name__}'")

    def __truediv__(self, other) -> "Vector":
        # division with other Vectors
        if other.__class__ == self.__class__:
            return Vector(self.x / other.x, self.y / other.y)
        # divison with Float or Int
        elif other.__class__ == int or other.__class__ == float:
            return Vector(self.x / other, self.y / other)
        else:
            raise TypeError(
                f"unsupported operand type(s) for /: '{self.__class__.__name__}' and '{other.__class__.__name__}'")

    def clamp(self, size: float = 1.0) -> "Vector":
        """
        crop the vector to a box  size Size

        Returns:
            Vector: The cropped Vector
        """
        if self.x < self.y:
            return self / (self.y * size)
        return self / (self.x * size)

    @property
    def magnitude(self) -> float:
        """
        return the magnitude of the vector
        """
        return math.sqrt(self.sqrMagnitude)

    @property
    def sqrMagnitude(self) -> float:
        """
        return the magnitude squared, considerably faster to be used for comparisons
        """
        return self.x**2 + self.y**2

    @property
    def normalized(self) -> "Vector":
        """
        return the vector divided by the magnitude
        """
        return self / self.magnitude

    def copy(self) -> "Vector":
        """
        Shallow copy of self

        Returns:
            Vector: A copy of self
        """
        return self.__class__(self.x, self.y)
