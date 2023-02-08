#!/usr/bin/python3
"""
A class named Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class that describes a square
    """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return (f"[Rectangle] {self.__size}/{self.__size}")
