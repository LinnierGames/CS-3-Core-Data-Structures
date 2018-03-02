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
        """Return True if this queue is empty, or False otherwise."""
        return self.length() == 0

    def length(self):
        """Return the number of items in this queue."""
        return self.list.length()

    def enqueue(self, item):
        self.list.append(item)

    def front(self):
        if self.is_empty():
            return None

        return self.list.get_at_index(0)

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty")

        dequeued_item = self.front()
        self.list.delete(dequeued_item)

        return dequeued_item


# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""

        return self.length() == 0

    def length(self):
        """Return the number of items in this queue."""

        return len(self.list)

    def enqueue(self, item):
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        if self.is_empty():
            return None

        return self.list[0]

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty")

        dequeued_item = self.front()
        self.list.remove(dequeued_item)

        return dequeued_item


# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
Queue = ArrayQueue
# Queue = ArrayQueue
