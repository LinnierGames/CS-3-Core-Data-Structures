#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_recursive(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # if item is found
    if array[index] == item:
        return index
    else:
        # not found and has reached the end of the array
        if index == len(array) -1:
            return None
        else:
            # call recursively
            return linear_search_recursive(array, item, index +1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    length = len(array)
    offset = 0
    lower = 0
    upper = length -1

    while lower != upper:
        midpoint = length // 2 +offset
        lower_adjacent_item = array[midpoint -1]
        upper_adjacent_item = array[midpoint]

        # Check if item is at the midpoint
        if item == lower_adjacent_item:
            return midpoint -1
        elif item == upper_adjacent_item:
            return midpoint
        elif length == 2:  # if item is not at midpoint and the length is 2, item not found
            return None

        if item > lower_adjacent_item:  # discard lower half
            offset += midpoint - lower
            lower = midpoint
        else:  # discard upper half
            upper = midpoint

        length = upper - lower +1

        print lower, length, upper

    if array[lower] == item:
        return lower
    else:
        return None


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
