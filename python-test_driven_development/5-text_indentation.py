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
    flag = 0
    for char in text:
        if flag == 1 and char == " ":
            continue
        flag = 0
        if char == '.' or char == '?' or char == ':':
            print(char, end='\n\n')
            flag = 1
        else:
            print(char, end='')
