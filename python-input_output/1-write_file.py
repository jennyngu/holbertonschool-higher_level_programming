#!/usr/bin/python3
"""
A method that writes to a text file
"""


def write_file(filename="", text=""):
    """
    Writes the given text to specified file

    Return: number of characters written to the file
    """
    with open(filename, 'w', encoding="utf-8") as writer:
        return(writer.write(text))
