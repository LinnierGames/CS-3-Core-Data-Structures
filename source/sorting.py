#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    for index in range(0, len(items) -1):
        element = items[index]
        adjacent_element = items[index +1]

        if element > adjacent_element:
            return False

    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    while True:
        # iterate throughout the items and swap out of ordered pairs
        for index in range(0, len(items) -1):
            adjacent_index = index +1
            element = items[index]
            adjacent_element = items[adjacent_index]

            # swap the elements if the are not in order
            if element > adjacent_element:
                items[index] = adjacent_element
                items[adjacent_index] = element

                continue
        else:

            # if the iteration completed without swapping, the list is sorted
            break


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    length = len(items)

    # iterate throughout the items once
    for index in range(0, length):
        current_min_value = items[index]
        current_min_index = index

        # find the smallest value between index and the end of the list
        for selection_index in range(index +1, length):
            current_selection_value = items[selection_index]

            # update the smallest value if a smaller value is found
            if current_selection_value < current_min_value:
                current_min_value = current_selection_value
                current_min_index = selection_index

        # swap values
        items[current_min_index] = items[index]
        items[index] = current_min_value


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    length = len(items)

    # iterate throughout the items once
    for index in range(0, length):

        for insert_index in range(index, 0, -1):
            current_checking_value = items[insert_index]
            current_adjacent_value = items[insert_index -1]

            if current_checking_value > current_adjacent_value:
                break

            # swap
            items[insert_index -1] = current_checking_value
            items[insert_index] = current_adjacent_value


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    list_a_index = 0
    list_a_last_index = len(items1) -1
    list_b_index = 0
    list_b_last_index = len(items2) -1

    # other words list c
    merged_list = list()
    while True:

        # list a is not finished
        if list_a_index <= list_a_last_index:

            # list b is not finished
            if list_b_index <= list_b_last_index:
                current_a_value = items1[list_a_index]
                current_b_value = items2[list_b_index]

                # find smallest
                if current_a_value <= current_b_value:
                    merged_list.append(current_a_value)
                    list_a_index += 1
                else:
                    merged_list.append(current_b_value)
                    list_b_index += 1

            # list b is finished: append all of a onto list c
            else:
                # TODO: merge all items at once vs throughout iterations of the while loop
                list_a_value = items1[list_a_index]
                merged_list.append(list_a_value)
                list_a_index += 1

        # list a is finished
        else:

            # list b is not finished
            if list_b_index <= list_b_last_index:

                # append all of list b onto list c
                # TODO: merge all items at once vs throughout iterations of the while loop
                list_b_value = items2[list_b_index]
                merged_list.append(list_b_value)
                list_b_index += 1

            # list b and a are finished:
            else:
                break

    return merged_list


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    # split items list into approximately equal halves
    half_index = len(items) // 2
    list_a = items[:half_index]
    list_b = items[half_index:]

    # sort each half using any other sorting algorithm
    list_a.sort()
    list_b.sort()

    # merge sorted halves into one list in sorted order
    merged_list = merge(list_a, list_b)

    return merged_list


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    # items is already sorted
    if len(items) <= 1:
        return items

    # split items list into approximately equal halves
    half_index = len(items) // 2
    list_a = items[:half_index]
    list_b = items[half_index:]

    # merge recursively called sorted halves into one list in sorted order
    return merge(merge_sort(list_a), merge_sort(list_b))


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of counts with a slot for each number in input range
    # TODO: Loop over given numbers and increment each number's count
    # TODO: Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    sorting each bucket, and combining contents of all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list


def random_ints(count=20, min=1, max=50):
    """Return a list of `count` integers sampled uniformly at random from
    given range [`min`...`max`] with replacement (duplicates are allowed)."""
    import random
    return [random.randint(min, max) for _ in range(count)]


def test_sorting(sort=bubble_sort, num_items=20, max_value=50):
    """Test sorting algorithms with a small list of random items."""
    # Create a list of items randomly sampled from range [1...max_value]
    items = random_ints(num_items, 1, max_value)
    print('Initial items: {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))

    # Change this sort variable to the sorting algorithm you want to test
    # sort = bubble_sort
    print('Sorting items with {}(items)'.format(sort.__name__))
    sort(items)
    print('Sorted items:  {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))


def main():
    a = [1,3,5,7]
    b = [2,2,5,8]

    c = merge(a, b)

    print c

    print split_sort_merge([7,1,3,2,5,2,8,5])


    print merge_sort([1000,7,1,1,2,5,2,1,5,1])

    return
    """Read command-line arguments and test sorting algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name

    if len(args) == 0:
        script = sys.argv[0]  # Get script file name
        print('Usage: {} sort num max'.format(script))
        print('Test sorting algorithm `sort` with a list of `num` integers')
        print('    randomly sampled from the range [1...`max`] (inclusive)')
        print('\nExample: {} bubble_sort 10 20'.format(script))
        print('Initial items: [3, 15, 4, 7, 20, 6, 18, 11, 9, 7]')
        print('Sorting items with bubble_sort(items)')
        print('Sorted items:  [3, 4, 6, 7, 7, 9, 11, 15, 18, 20]')
        return

    # Get sort function by name
    if len(args) >= 1:
        sort_name = args[0]
        # Terrible hack abusing globals
        if sort_name in globals():
            sort_function = globals()[sort_name]
        else:
            # Don't explode, just warn user and show list of sorting functions
            print('Sorting function {!r} does not exist'.format(sort_name))
            print('Available sorting functions:')
            for name in globals():
                if name.find('sort') >= 0:
                    print('    {}'.format(name))
            return

    # Get num_items and max_value, but don't explode if input is not an integer
    try:
        num_items = int(args[1]) if len(args) >= 2 else 20
        max_value = int(args[2]) if len(args) >= 3 else 50
        # print('Num items: {}, max value: {}'.format(num_items, max_value))
    except ValueError:
        print('Integer required for `num` and `max` command-line arguments')
        return

    # Test sort function
    test_sorting(sort_function, num_items, max_value)


if __name__ == '__main__':
    main()
