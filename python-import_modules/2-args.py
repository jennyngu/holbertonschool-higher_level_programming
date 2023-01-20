#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_length = len(sys.argv)
    if arg_length == 1:
        print("0 arguments.")
    elif arg_length == 2:
        print("{} argument:".format(arg_length - 1))
        print("{}: {}".format(arg_length - 1, sys.argv[1]))
    else:
        print("{} arguments:".format(arg_length - 1))
        for index, arg in enumerate(sys.argv[1:]):
            print("{}: {}".format(index + 1, arg))
