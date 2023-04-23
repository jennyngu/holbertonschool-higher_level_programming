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

    def update(self, *args, **kwargs):
        """
        Args go through *args to assign an argument to the according attributes
        in the given order.
        If args is given in key, value pairs, arg goes through **kwargs
        """
        for key, value in kwargs.items():
            if key == "size":
                self.size = value
            elif key == "x":
                self.x = value
            elif key == "y":
                self.y = value
            elif key == "id":
                self.id = value
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]

    def to_dictionary(self):
        """
        Returns the Square dictionary with only attribute names
        """
        new_dict = {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
            }
        return new_dict

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
