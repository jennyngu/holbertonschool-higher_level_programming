#!/usr/bin/python3
"""
A function that converts an object to JSON representation
"""
import json


def to_json_string(my_obj):
    """
    Return: JSON representation of an object(string)
    """
    return(json.dumps(my_obj))
