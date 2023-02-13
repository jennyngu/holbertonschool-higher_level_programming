#!/usr/bin/python3
"""
The base model/class used for other shapes
"""

class Base:
    """
    A class that defines the basis of shapes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Sets the id of an instance of Base
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
