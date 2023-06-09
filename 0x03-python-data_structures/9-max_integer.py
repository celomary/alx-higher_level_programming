#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_ = my_list[0]
    for num in my_list[1:]:
        if max_ < num:
            max_ = num
    return max_
