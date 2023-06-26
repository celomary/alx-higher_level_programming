#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = [0] * list_length
    index = 0
    while index < list_length:
        try:
            new_list[index] = my_list_1[index] / my_list_2[index]
        except (TypeError, ValueError):
            print('wrong type')
        except ZeroDivisionError:
            print('division by 0')
        except IndexError:
            print('out of range')
        index += 1
    return new_list
