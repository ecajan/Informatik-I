#!/usr/bin/env python3

def list_unique(elements):
    my_set = set()
    for x in elements:
        my_set.add(x)
    my_list = []
    for x in my_set:
        my_list.append(x)
    return my_list

