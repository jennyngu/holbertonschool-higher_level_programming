#!/usr/bin/python3
"""
A function that returns the dict description with simple data structure
for JSON serialisation of an object
"""


def class_to_json(obj):
    """
    Return: dict of data structure
    """
    return(obj.__dict__)
