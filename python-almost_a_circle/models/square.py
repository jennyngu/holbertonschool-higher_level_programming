#!/usr/bin/python3
"""
A class named Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class that inherits methods and attributes from Rectangle
    and defines a square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Instantiates a new object
        """
        super().__init__(size, size, x, y, id)
        self.width = self.height = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = self.height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
