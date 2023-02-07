#!/usr/bin/python3
"""
Checks if an object is an instance of a class
that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class
    that has previously inherited from the specified class

    obj: object to check
    a_class: class to check
    Return: True if is instance, False otherwise
    """
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
