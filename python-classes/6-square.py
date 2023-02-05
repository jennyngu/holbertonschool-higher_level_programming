#!/usr/bin/python3
"""Defines a class named Square"""


class Square:
    """Inititalises the square with the given size"""
    def __init__(self, size=0):
        if type(size) == int and size >= 0:
            self.__size = size
        elif type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    """Property getter to retrieve size"""
    @property
    def size(self):
        return self.__size

    """Property setter to set size"""
    @size.setter
    def size(self, value):
        if type(value) == int and value >= 0:
            self.__size = value
        elif type(value) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    """Initialises the position within the square"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    """Property getter to retrieve position"""
    @property
    def position(self):
        return self.__position

    """Property setter to set position"""
    @position.setter
    def position(self, value):
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] > 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    """Represents the area of the square"""
    def area(self):
        return self.__size ** 2

    """Prints the designated square area with '#' symbols"""
    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.position[1]):
            print()
        for j in range(self.__size):
            print(' ' * self.position[0], end='')
            print('#' * self.__size)
