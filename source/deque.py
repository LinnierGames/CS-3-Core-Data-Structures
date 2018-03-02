#!python

from linkedlist import LinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """
        Implement is_empty - check if the deque is empty
        :return: bool
        """
        pass

    def length(self):
        """
        Implement length - return the number of items in the deque
        :return: int
        """
        pass

    def push_front(self, item):
        """
        Implement push_front(item) - insert item at the front of the deque
        :return: void
        """
        pass

    def push_back(self, item):
        """
        Implement push_back(item) - insert item at the back of the deque
        :return: void
        """
        pass

    def front(self):
        """
        Implement front - return the item at the front of the deque
        :return: int
        """
        pass

    def back(self):
        """
        Implement back - return the item at the back of the deque
        :return: int
        """
        pass

    def pop_front(self):
        """
        Implement pop_front - remove and return the item at the front of the deque
        :return: int
        """
        pass

    def pop_back(self):
        """
        Implement pop_back - remove and return the item at the back of the deque
        :return: int
        """
        pass

