#!/usr/bin/python
def remove_char_at(str, n):
    if len(str) < n or n < 0:
        return str[:]
    return str[:n] + str[n+1:]
