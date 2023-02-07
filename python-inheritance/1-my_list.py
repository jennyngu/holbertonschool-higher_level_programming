#!/usr/bin/python3
"""
A class that inherits from the object list
"""


class MyList(list):
    """
    A class that defines a list
    """
    def print_sorted(self):
        """
        Prints a sorted list

        self: it self
        """
        print(sorted(self))
