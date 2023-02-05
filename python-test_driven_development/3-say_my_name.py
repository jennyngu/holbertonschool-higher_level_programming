#!/usr/bin/python3
"""
A function that prints the given name
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a name

    first_name: a first name
    last_name: a last name
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
