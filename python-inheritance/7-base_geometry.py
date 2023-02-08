#!/usr/bin/python3
"""
A class named BaseGeometry
"""


class BaseGeometry:
    """
    A class that describes a shape
    """
    def area(self):
        """
        Raises an exception message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Checks to see if a given value is an integer
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
