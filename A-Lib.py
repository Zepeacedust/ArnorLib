#!/usr/bin/env python
"""
Random stuff sem ég nota oft og nenni ekki að skrifa oft
"""
__author__ = "Arnór Friðriksson"
__version__ = "1.0.0"

import math


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


class PrioQueue:
    def __init__(self, key=int):
        self.root = None
        self.key = key

    def getEmpty(self):
        return self.root == None
    empty = property(getEmpty)

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
            if self.key(element.data) <= self.key(head.data):
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

    def pop(self):
        if self.root == None:
            raise IndexError("pop from empty queue")
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

    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __sub__(self, other):
        return Vector(self.x-other.x, self.y-other.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Vector(self.x / other, self.y / other)

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
        """
        return this vector scaled to a length of 1
        """
        return self / self.magnitude


def CountList(L):
    """
    Args:
        L: list
    Returns:
        Dictionary where keys are indexes in the list and values are how many times they occur
    """
    counted = {}
    for x in L:
        if x in counted.keys():
            counted[x] += 1
        else:
            counted[x] = 1
    return counted


if __name__ == "__main__":
    assert Vector(1, 2) * 3 == Vector(3, 6)
    assert CountList([1, 1, 1, 1, 2, 2, 2]) == {1: 4, 2: 3}