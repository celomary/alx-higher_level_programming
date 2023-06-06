#!/usr/bin/python3
for i in range(0, 100):
    print('{}'.format(i), end=', ' if i + 1 < 100 else '')
