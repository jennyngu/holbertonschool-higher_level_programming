#!/usr/bin/python3
"""
A class named Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class that describes a rectangle
    """
    def __init__(self, width, height):
        """
        Instantiation of a rectangle

        width: width of rectangle
        height: height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
