#!/usr/bin/python3
"""
Lists attributes and methods of an object
"""


def lookup(obj):
    """
    Returns a list of available attributes and method of an object
    """
    list = dir(obj)
    return list
