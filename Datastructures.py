#!/usr/bin/env python
"""
Random datastructures sem ég nota oft og nenni ekki að skrifa oft
"""
__author__ = "Arnór Friðriksson"
__version__ = "1.0.0"


import Wrappers

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
