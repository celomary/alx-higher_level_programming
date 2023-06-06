#!/usr/bin/python3
for i in range(26):
    print('{}'.format(chr([65, 97][i % 2 == 0] + 25 - i)), end='')
