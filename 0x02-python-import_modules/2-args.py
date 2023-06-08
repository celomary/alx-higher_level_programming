#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    args = argv[1:]
    print("{} arguments:".format(len(args)))
    for index, arg in enumerate(args):
        print("{}: {}".format(index+1, arg))
