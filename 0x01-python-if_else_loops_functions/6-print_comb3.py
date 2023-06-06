#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i + 1, 10):
        print("{}{}".format(i, j), end=", " if j + 1 < 10 else "")
    print(end=", " if i + 1 < 9 else "\n")
