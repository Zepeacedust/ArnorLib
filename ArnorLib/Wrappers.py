#!/usr/bin/env python
"""
Random wrappers sem ég nota oft og nenni ekki að skrifa oft
"""
__author__ = "Arnór Friðriksson"
__version__ = "1.0.1"

from functools import wraps
import time


def Time(func):
    @wraps(func)
    def TimeWrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return TimeWrapper


def SameClass(func):
    @wraps(func)
    def SameClassWrapper(self, other):
        if self.__class__ == other.__class__:
            return func(self, other)
        else:
            return False
    return SameClassWrapper
