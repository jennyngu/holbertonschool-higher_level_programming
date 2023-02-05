#!/usr/bin/python3
"""
Adds 2 new lines to a piece of text
"""


def text_indentation(text):
    """
    Adds 2 new lines after encounter with ., ?, and : characters

    text: text to alter
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    else:
        text = text.replace('. ', '.\n\n')
        text = text.replace('? ', '?\n\n')
        text = text.replace(': ', ':\n\n')
    print(text)
