#!/usr/bin/python3
"""
A function that creates an object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    Return: object created from specified JSON file
    """
    with open(filename, encoding="utf-8") as obj_from_json:
        return(json.load(obj_from_json))
