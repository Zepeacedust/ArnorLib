#!/usr/bin/env python
"""
Random stuff sem ég nota oft og nenni ekki að skrifa oft
"""
__author__ = "Arnór Friðriksson"
__version__ = "1.0.0"

import math
import Wrappers
from typing import Any, Dict, List


class TreeNode:
    """
    Class fyrir binary tree
    """

    def __init__(self, data, key=int):
        """
        Class fyrir binary tree

        Args:
            data (Any): Holds any data
            key (Function, optional): Method to call to sort Tree. Defaults to int.
        """
        self.data = data
        self.key = key
        self.left = None
        self.right = None

    @Wrappers.SameClass
    def __eq__(self, other:"TreeNode") -> bool:
        return self.key(self.data) == other.key(other.data)

    @Wrappers.SameClass
    def __gt__(self, other:"TreeNode") -> bool:
        return self.key(self.data) > other.key(other.data)

    @Wrappers.SameClass
    def __lt__(self, other:"TreeNode") -> bool:
        return self.key(self.data) < other.key(other.data)

    @Wrappers.SameClass
    def __ge__(self, other:"TreeNode") -> bool:
        return self.key(self.data) >= other.key(other.data)

    @Wrappers.SameClass
    def __le__(self, other:"TreeNode") -> bool:
        return self.key(self.data) <= other.key(other.data)

    @Wrappers.SameClass
    def __ne__(self, other:"TreeNode") -> bool:
        return self.key(self.data) != other.key(other.data)

    @property
    def isLeaf(self) -> bool:
        return self.left == None and self.right == None


class BinaryTree:
    def __init__(self, key=int):
        self.root = None
        self.key = key

    @property
    def empty(self) -> bool:
        return self.root == None

    def add(self, data) -> int:
        """
        Add TreeNode with data to list checking if it is empty 
        """
        element = TreeNode(data)
        # Classic add í Binary tree
        if self.root == None:
            # Ef tré er tómt
            self.root = element
            return 0
        else:
            return self.__addElement(element)

    def __addElement(self, element:TreeNode):
        """
        Adds TreeNode element to the queue

        Args:
            element (TreeNode): Node to be added

        Returns:
            None
        """
        head = self.root
        while True:
            # Finna réttan stað og setja node þar
            if element <= head:
                if head.left == None:
                    head.left = element
                    return 0
                else:
                    head = head.left
            else:
                if head.right == None:
                    head.right = element
                    return 0
                else:
                    head = head.right


class PrioQueue(BinaryTree):
    def __init__(self, key=int):
        BinaryTree.__init__(self, key=int)

    def pop(self):
        if self.empty:
            raise IndexError("pop from empty tree.")
        head = self.root
        last = None
        while head.left != None:
            last = head
            head = head.left
        if last == None:
            self.root = head.right
        else:
            last.left = head.right
        data = head.data
        del head
        return data


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
            return Vector(self.x / other.x, self.y / other.x)
        # divison with Float or Int
        elif other.__class__ == int or other.__class__ == float:
            return Vector(self.x / other, self.y / other)
        else:
            raise TypeError(
                f"unsupported operand type(s) for /: '{self.__class__.__name__}' and '{other.__class__.__name__}'")
    
    def clamp(self, size:float = 1.0) -> "Vector":
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


# telja öll indexes í lista
def CountList(L:list) -> Dict[Any, int]:
    counted = {}
    for x in L:
        if x in counted.keys():
            counted[x] += 1
        else:
            counted[x] = 1
    return counted

def WeightedMiddle(L:list) -> List[Any]:
    """find the weighted middle of a list

    Args:
        L: list of tuples, the first index is the data and the second is the weight

    Returns:
        Any: the first index of the weighted middle of the list
    """

    tip = 0
    tail = 0
    tipPos = 0
    tailPos = len(L) - 1
    while tipPos != tailPos:
        if tail + L[tailPos][1] < tip + L[tipPos][1]:
            tail += L[tailPos][1]
            tailPos -= 1
        else:
            tip += L[tipPos][1]
            tipPos += 1
    return L[tailPos][0]


if __name__ == "__main__":
    print(Vector(1, 2).clamp())
