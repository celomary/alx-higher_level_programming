#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    my_list = [0 for _ in range(max(len(tuple_a), len(tuple_b)))]
    for idx in range(max(len(tuple_a), len(tuple_b))):
        my_list[idx] = tuple_a[idx] if len(tuple_a) > idx else 0
        my_list[idx] += tuple_b[idx] if len(tuple_b) > idx else 0
    return tuple(my_list)
