#!/usr/bin/python3
"""Defines a class named Square"""


class Square:
    """Represents a square with given size"""
    def __init__(self, size=0):
        if type(size) == int and size >= 0:
            self.__size = size
        elif type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
