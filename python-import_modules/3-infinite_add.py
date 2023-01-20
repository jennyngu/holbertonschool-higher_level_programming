#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg_length = len(sys.argv)
    sum = 0
    for index in range(1, arg_length):
        sum = sum + int(sys.argv[index])
    print("{}".format(sum))
