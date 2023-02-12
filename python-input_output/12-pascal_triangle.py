#!/usr/bin/python3
"""
A function that returns a list of lists of integers
representing Pascal's triangle
"""


def pascal_triangle(n):
    """
    Creates new lists which represent rows in Pascal's triangle
    up to the size of n

    Return: Pascal's triangle
    """
    if n <= 0:
        return []

    triangle = [0] * n
    for i in range(n):
        new_list = [0] * (i + 1)
        new_list[0] = 1
        new_list[len(new_list) - 1] = 1

        for j in range(1, i):
            if j > 0 and j < len(new_list):
                num_a = triangle[i - 1][j]
                num_b = triangle[i - 1][j - 1]
                new_list[j] = num_a + num_b
        triangle[i] = new_list
    return triangle
