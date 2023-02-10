#!/usr/bin/python3
"""
A function that converts a JSON string to an object (Python data structure)
"""
import json

def from_json_string(my_str):
    """
    Return: object representated by a JSON string
    """
    return(json.loads(my_str))
