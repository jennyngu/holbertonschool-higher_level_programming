#!/usr/bin/python3
"""
Checks if an object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    Checks if object is an instance of a_class

    obj: object to check
    a_class: class to check
    Returns True if obj is exactly an instance of a_class, False otherwise
    """
    if type(obj) == a_class:
        return True
    else:
        return False
