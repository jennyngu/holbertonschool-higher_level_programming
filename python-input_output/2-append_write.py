#!/usr/bin/python3
"""
A method that appends string to text file
"""


def append_write(filename="", text=""):
    """
    Appends given string to the end of a textfile

    Return: number of characters added to the file
    """
    with open(filename, 'a', encoding="utf-8") as writer:
        return(writer.write(text))
