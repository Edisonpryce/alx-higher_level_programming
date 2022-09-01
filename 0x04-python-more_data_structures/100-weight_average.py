#!/usr/bin/python3
def weight_average(my_list=[]):
    div = 0
    add_mul = 0

    if not my_list:
        return 0

    for a, b in my_list:
        mul = 0
        mul = a * b
        add_mul += mul
        div += b

    average = add_mul / div
    return average
