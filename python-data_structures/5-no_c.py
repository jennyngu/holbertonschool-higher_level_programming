#!/usr/bin/python3
def no_c(my_string):
    for letter in range(len(my_string)):
        if my_string[letter] == 'c' or my_string[letter] == 'C':
            return my_string[:letter] + my_string[letter + 1:]
