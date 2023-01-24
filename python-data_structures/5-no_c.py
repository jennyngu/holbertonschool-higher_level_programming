#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    letter_c = 'cC'
    for letter in range(len(my_string)):
        if my_string[letter] not in letter_c:
            new_string = new_string + my_string[letter]
    return new_string
