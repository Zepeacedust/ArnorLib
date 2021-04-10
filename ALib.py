#!/usr/bin/env python
"""
Random stuff sem ég nota oft og nenni ekki að skrifa oft
"""
__author__ = "Arnór Friðriksson"
__version__ = "1.0.0"

import math
from functools import wraps

def SameClass(func):
    @wraps(func)
    def SameClassWrapper(self, other):
        if self.__class__ == other.__class__:
            return func(self,other)
        else:
            return False
    return SameClassWrapper



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
    
    @SameClass
    def __eq__(self, other):
        return self.key(self.data) == self.key(other.data)

    @SameClass
    def __gt__(self, other):
        return self.key(self.data) > self.key(other.data)
    
    @SameClass
    def __lt__(self, other):
        return self.key(self.data) < self.key(other.data)
    
    @SameClass
    def __ge__(self, other):
        return self.data >= other.data
    
    @SameClass
    def __le__(self,other):
        return self.data <= other.data
    
    @SameClass
    def __ne__(self,other):
        return self.data != other.data

    @property
    def isLeaf(self):
        return self.left == None and self.right == None


class BinaryTree:
    def __init__(self, key=int):
        self.root = None
        self.key = key

    @property
    def empty(self):
        return self.root == None

    def add(self, data):
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
            self.__addElement(element)

    def __addElement(self, element):
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

    def __str__(self):
        return "{}({},{})".format(self.__class__.__name__, self.x, self.y)
    
    @SameClass
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


    def __add__(self, other):
        if other.__class__ == self.__class__:
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("unsupported operand type(s) for +: '{}' and '{}'".format(
                self.__class__.__name__, other.__class__.__name__))

    def __sub__(self, other):
        if other.__class__ == self.__class__:
            return Vector(self.x - other.x, self.y - other.y)
        else:
            raise TypeError("unsupported operand type(s) for -: '{}' and '{}'".format(
                self.__class__.__name__, other.__class__.__name__))

    def __mul__(self, other):
        if other.__class__ == self.__class__:
            return Vector(self.x * other.x, self.y * other.y)
        elif other.__class__ == int or other.__class__ == float:
            return Vector(self.x * other, self.y * other)
        else:
            raise TypeError("unsupported operand type(s) for *: '{}' and '{}'".format(
                self.__class__.__name__, other.__class__.__name__))

    def __truediv__(self, other):
        #division with other Vectors
        if other.__class__ == self.__class__:
            return Vector(self.x / other.x, self.y / other.x)
        #divison with Float or Int
        elif other.__class__ == int or other.__class__ == float:
            return Vector(self.x / other, self.y / other)
        else:
            raise TypeError("unsupported operand type(s) for /: '{}' and '{}'".format(
                self.__class__.__name__, other.__class__.__name__))

    @property
    def magnitude(self):
        """
        return the magnitude of the vector
        """
        return math.sqrt(self.sqrMagnitude)

    @property
    def sqrMagnitude(self):
        """
        return the magnitude squared, considerably faster to be used for comparisons
        """
        return self.x**2 + self.y**2

    @property
    def normalized(self):
        return self / self.magnitude


# telja öll indexes í lista
def CountList(L):
    counted = {}
    for x in L:
        if x in counted.keys():
            counted[x] += 1
        else:
            counted[x] = 1
    return counted

if __name__ == "__main__":
    assert Vector(1, 2) * 3 == Vector(3, 6)