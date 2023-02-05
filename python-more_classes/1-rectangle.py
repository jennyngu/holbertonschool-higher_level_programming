#!/usr/bin/python3
"""Defines a class named Rectangle"""


class Rectangle:
    """
    A class that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initialises the rectangle with the given dimensions
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Property getter to retrieve width size
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Property setter to set width size
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Property getter to retrieve height
        """
        self.__height = height

    @height.setter
    def height(self, value):
        """
        Property setter to set the height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
