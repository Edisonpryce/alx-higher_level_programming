#!/usr/bin/python3
""" In a list of Unsorted integers, finds a peak
"""


def find_peak(list_of_int):
    """
    Args:
        list_of_integers: we would find the peak in this list
    Returns: none if list_of_int is empty else return list_of_int
    """
    size_l = len(list_of_int)
    mid_l = size_l
    mid = size_l // 2

    if size_l == 0:
        return None

    while 1:
        mid_l = mid_l // 2
        if (mid < size_l - 1 and
                list_of_int[mid] < list_of_int[mid + 1]):
            if mid_l // 2 == 0:
                mid_l = 2
            mid = mid + mid_l // 2
        elif mid_l > 0 and list_of_int[mid] < list_of_int[mid - 1]:
            if mid_l // 2 == 0:
                mid_l = 2
            mid = mid - mid_l // 2
        else:
            return list_of_int[mid]
