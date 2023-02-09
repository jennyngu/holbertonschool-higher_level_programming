#!/usr/bin/python3
"""
A method that reads a text file and prints it to stdout
"""


def read_file(filename=""):
    """
    Reads a given file and prints its contents to stdout
    """
    with open(filename, encoding="utf-8") as reader:
        read_file = reader.read()
        print(read_file, end='')
