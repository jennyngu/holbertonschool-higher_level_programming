#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = dict(sorted(a_dictionary.items()))
    if a_dictionary is None:
        return
    else:
        for key in sorted_dict:
            print("{}: {}".format(key, sorted_dict[key]))
