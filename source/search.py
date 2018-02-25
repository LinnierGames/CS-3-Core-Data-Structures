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
    left = 0
    right = length -1

    # split array until left bound and right bound are equal
    while left != right:
        length = right - left +1
        midpoint = length // 2 +left

        # is item after/before midpoint
        if item >= array[midpoint]:
            # discard left half
            left = midpoint
        else:
            # discard right half
            right = midpoint -1

    # does split array, of one, equal item?
    if array[left] == item:
        return left
    else:
        return None


def binary_search_recursive(array, item, left=None, right=None):
    # setup left and right bounds
    if left is not None:
        length = right - left + 1
        midpoint = length // 2 + left
    else:
        length = len(array)
        left = 0
        right = length -1
        midpoint = length // 2

    # does left and right equal the item
    if length == 1:
        if item != array[left]:
            # not found, does not exist
            return None
        else:
            # found
            return left

    # is item after/before midpoint
    if item >= array[midpoint]:
        # discard left
        return binary_search_recursive(array, item, midpoint, right)
    else:
        # discard right
        return binary_search_recursive(array, item, left, midpoint -1)



































