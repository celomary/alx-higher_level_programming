#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    is_newline = False
    for c in text:
        is_newline = False
        print(c, end='')
        if c in ".?:":
            print("\n")
            is_newline = True
    if not is_newline:
        print()
