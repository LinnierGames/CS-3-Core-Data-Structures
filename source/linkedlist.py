#!python

import pdb

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.n = None
        self.p = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedListIterator(object):

    def __init__(self, node):
        self.node = node

    def next(self):
        if self.node.n is not None:
            return self.node
        else:
            raise StopIteration()


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0  # Number of nodes
        # Append the given items
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def __len__(self):
        return self.size

    def __iter__(self):
        return LinkedListIterator(self.head)

    def __getitem__(self, index):
        try:
            return self.get_at_index(index)
        except ValueError as err:
            raise err

    def __setitem__(self, index, value):
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))

        curr_node = self.head

        # iterate throughout the whole list
        while True:

            # exhausted the linked list
            if curr_node is None:
                return None

            # continue iterating
            else:

                # counter, index, has hit zero
                if index == 0:

                    # replace the data
                    curr_node.data = value

                # decrease the counter, index, and iterate the curr_node
                else:
                    curr_node = curr_node.n
                    index -= 1

    def items(self):
        """Return a list of all items in this linked list.
        Best and worst case running time: Theta(n) for n items in the list
        because we always need to loop through all n nodes."""

        # Create an empty list of results
        result = []  # Constant time to create a new list

        # Start at the head node
        node = self.head  # Constant time to assign a variable reference

        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Always n iterations because no early exit

            # Append this node's data to the results list
            result.append(node.data)  # Constant time to append to a list
            node = node.n  # Constant time to reassign a variable

        # Now result contains the data from all nodes
        return result  # Constant time to return a list

    def is_empty(self):
        """Return True if this linked list is empty, or False."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Best and worst case running time: ??? under what conditions? [TODO]"""

        # Node counter initialized to zero
        return self.size

    def get_at_index(self, index):
        """Return the item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""

        # Check if the given index is out of range and if so raise an error
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))

        curr_node = self.head

        # iterate throughout the whole list
        while True:

            # exhausted the linked list
            if curr_node is None:
                return None

            # continue iterating
            else:

                # counter, index, has hit zero
                if index == 0:

                    # return the data
                    return curr_node.data

                # decrease the counter, index, and iterate the curr_node
                else:
                    curr_node = curr_node.n
                    index -= 1

    def insert_at_index(self, index, item):
        """Insert the given item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""

        # Check if the given index is out of range and if so raise an error
        if not (0 <= index <= self.size):
            raise ValueError('List index out of range: {}'.format(index))

        curr_node = self.head
        inserted = False

        new_node = Node(item)

        # edge: insert at the head
        if index == 0:

            # edge: if inserting in an empty list
            if self.head is None:

                # set the head and tail to the new_node
                self.head = self.tail = new_node

            # base: inserting at the beginning of list.size > 1
            else:
                new_node.n = self.head
                self.head.p = new_node

                # reset head
                self.head = new_node

        # edge: insert at the tail
        elif index == self.size:
            self.tail.n = new_node
            new_node.p = self.tail

            # reset tail
            self.tail = new_node

        # base: insert in the middle
        else:
            # iterate to the desired index while the counter, index is > 0
            while index > 0:
                curr_node = curr_node.n
                index -= 1

            # insert the new_node, attach the prev and the cur node to new_node
            previous_node = curr_node.p
            previous_node.n = new_node
            curr_node.p = new_node

            # update new_node to curr_node and previous_node
            new_node.n = curr_node
            new_node.p = previous_node

        self.size += 1

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Best and worst case running time: ??? under what conditions? [TODO]"""

        # insert at the size of the list
        self.insert_at_index(self.size, item)

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Best and worst case running time: ??? under what conditions? [TODO]"""

        # insert at the zero index
        self.insert_at_index(0, item)

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: Omega(1) if item is near the head of the list.
        Worst case running time: O(n) if item is near the tail of the list or
        not present and we need to loop through all n nodes in the list."""

        # Start at the head node
        node = self.head  # Constant time to assign a variable reference

        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Up to n iterations if we don't exit early

            # Check if this node's data satisfies the given quality function
            if quality(node.data):  # Constant time to call quality function

                # We found data satisfying the quality function, so exit early
                return node.data  # Constant time to return data

            # Skip to the next node
            node = node.n  # Constant time to reassign a variable

        # We never found data satisfying quality, but have to return something
        return None  # Constant time to return None

    def replace(self, old_item, new_item):
        """Replace the given old_item in this linked list with given new_item
        using the same node, or raise ValueError if old_item is not found.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""

        curr_node = self.head

        did_replace = False

        while curr_node is not None:
            if curr_node.data == old_item:
                curr_node.data = new_item
                did_replace = True
                break
            else:
                curr_node = curr_node.n

        if not did_replace:
            raise ValueError, 'did not find {}'.format(old_item)

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""

        # Start at the head node
        node = self.head

        # Create a flag to track if we have found the given item
        found = False

        # Loop until we have found the given item or the node is None
        while not found and node is not None:

            # Check if the node's data matches the given item
            if node.data == item:

                # We found data matching the given item, so update found flag
                found = True
            else:

                # Skip to the next node
                node = node.n

        # Check if we found the given item or we never did and reached the tail
        if found:

            # Check if we found a node in the middle of this linked list
            if node is not self.head and node is not self.tail:
                print "delete middle, {}".format(item)

                # Update the previous node to skip around the found node
                previous = node.p
                adjacent_node = node.n
                previous.n = adjacent_node

                # Unlink the adjacent nodes from the found node
                adjacent_node.p = previous

                # Unlink the found node from the adjacent nodes
                node.p = None
                node.n = None


            # Check if we found a node at the head
            elif node is self.head:
                print "delete head, h: {}".format(self.head)

                # Update head to the next node
                adjacent_node = node.n
                self.head = adjacent_node

                # if head is none, tail is also none
                if self.head is None:
                    self.tail = None

                # Unlink the found node from the next node
                if adjacent_node is not None:
                    adjacent_node.p = None

                node.n = None

            # Check if we found a node at the tail
            elif node is self.tail:
                print "delete tail, h: {}".format(self.tail)

                # Check if there is a node before the found node
                if node.p is not None:

                    # Unlink the previous node from the found node
                    previous = node.p
                    previous.n = None

                # Update tail to the previous node regardless
                self.tail = node.p

                # if head is none, tail is also none
                if self.tail is None:
                    self.head = None

                node.p = None

            self.size -= 1
        else:

            # Otherwise raise an error to tell the user that delete has failed
            raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print(ll)

    print('Appending items:')
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))

    print('Getting items by index:')
    for index in range(ll.size):
        item = ll.get_at_index(index)
        print('get_at_index({}): {!r}'.format(index, item))

    print('Deleting items:')
    ll.delete('B')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('A')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
