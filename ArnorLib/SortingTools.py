#!/usr/bin/env python
"""
utilities til að gera sorting algorithms
"""
__author__ = "Arnór Friðriksson"
__version__ = "1.0.1"


from typing import List


def merge(a: List, b: List, key=int) -> List:
    """
    Merge two sorted lists by key

    Args:
        a (List): List A
        b (List): List B 
        key (function, optional): key to sort by. Defaults to int.

    Returns:
        List: Merged List
    """     
    
    aPos = bPos = 0
    aLen = len(a)
    bLen = len(b)
    outList = []
    #zip together the lists
    while aPos < aLen and bPos < bLen:
        if key(a[aPos]) < key(b[bPos]):
            outList.append(a[aPos])
            aPos += 1
        else:
            outList.append(b[bPos])
            bPos += 1

    # if one list is empty fully append the other
    if aPos != aLen:
        outList += a[aPos:]
    elif bPos != bLen:
        outList += b[bPos:]
    return outList


def mergeLists(a: List[List], key=int) -> List[List]:
    # ensure that the number of lists is even
    if len(a) % 2 == 1:
        a.append(merge(a.pop(), a.pop(), key=key))

    outLists = []

    while a != []:
        outLists.append(merge(a.pop(), a.pop(), key=key))

    return outLists


def fullyCondense(a: List[List], key=int) -> List:
    while len(a) != 1:
        a = mergeLists(a, key=key)
    return a[0]
