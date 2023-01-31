#!/usr/bin/python3
"""Defines a class named Square """


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

    """Represents the area of the square"""
    def area(self):
        return self.__size ** 2

    """Prints the designated square area with '#' symbols"""
    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(1, self.__size + 1):
            for j in range(1, self.__size + 1):
                if j <= i:
                    print('#', end='')
                else:
                    print('#', end='')
            print()
