#!python

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""

        return self.length() == 0

    def length(self):
        """Return the number of items in this stack."""
        return self.list.length()

    def push(self, item):
        self.list.prepend(item)

    def peek(self):
        if self.is_empty():
            return None

        # the tail is the 'last' item in the stack
        return self.list.head.data

    def pop(self):
        if self.is_empty():
            raise ValueError('Empty list')

        # peek the last value before deleting
        data_popped = self.peek()
        self.list.delete(data_popped)

        return data_popped


# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""

        return self.length() == 0

    def length(self):
        """Return the number of items in this stack."""

        return len(self.list)

    def push(self, item):
        self.list.append(item)

    def peek(self):
        if self.is_empty():
            return None

        # subscript the last item in the list
        last_index = self.length() -1
        return self.list[last_index]

    def pop(self):
        if self.is_empty():
            raise ValueError('Empty list')

        # peek before deleting
        data_popped = self.peek()
        self.list.remove(data_popped)

        return data_popped


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
Stack = ArrayStack
# Stack = ArrayStack
