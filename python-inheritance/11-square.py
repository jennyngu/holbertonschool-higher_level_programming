#!/usr/bin/python3
"""
A class named Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class that describes a rectangle
    """
    def __init__(self, size):
        self.__size = size
        Rectangle.integer_validator(self, "size", size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return (f"[Square] {self.__size}/{self.__size}")
