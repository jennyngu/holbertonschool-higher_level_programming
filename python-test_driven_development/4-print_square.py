#!/usr/bin/python3
"""
Prints a square
"""


def print_square(size):
    """
    Prints a square of given size

    size: size of square
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            if j <= i:
                print('#', end='')
            else:
                print('#', end='')
        print()
