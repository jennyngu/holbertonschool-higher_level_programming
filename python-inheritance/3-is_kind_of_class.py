#!/usr/bin/python3
"""
Checks if an object an instance of, or if the object
is an instance of a class that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if object is an instance of a class
    or an instance of a class inherited from specified class

    obj: object to check
    a_class: class to check
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
