#!/usr/bin/python3
def uppercase(str):
    for char in str:
        char = ord(char)
        if 97 <= char <= 122:
            char = char - 32
        print("{:c}".format(char), end='')
    print("")
