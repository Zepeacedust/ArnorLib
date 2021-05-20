#!/usr/bin/env python
"""
Random stuff sem ég nota oft og nenni ekki að skrifa oft
"""
__author__ = "Arnór Friðriksson"
__version__ = "1.0.0"

from typing import Any, Dict, List


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
