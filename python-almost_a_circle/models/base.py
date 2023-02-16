#!/usr/bin/python3
"""
The base model/class used for other shapes
"""
import json


class Base:
    """
    A class that defines the basis of shapes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Sets the id of an instance of Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns a JSON string representation of a list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == "":
            return "[]"
        return json.dumps(list_dictionaries)
