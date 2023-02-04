#!/usr/bin/python3
"""
A function that adds two integers
"""


def add_integer(a, b=98):
    """
    Given two integers, returns the sum of a and b
    a: first argument
    b: second argument with a default value of 98

    Return: int(a) + int(b)
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(a) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
