#!python

from linkedlist import LinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedDeque(object):

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
        return self.length() == 0

    def length(self):
        return self.list.length()

    def push_front(self, item):
        """
        Add to the front of the queue
        """

        self.list.prepend(item)

    def push_back(self, item):
        """
        Add to the back of the queue
        :return: void
        """

        self.list.append(item)

    def front(self):
        """
        Peek the front of the queue
        """

        if self.is_empty():
            return None

        return self.list.get_at_index(0)

    def back(self):
        """
        Implement back - return the item at the back of the deque
        :return: int
        """

        if self.is_empty():
            return None

        back_index = self.length() -1
        return self.list.get_at_index(back_index)

    def pop_front(self):
        """
        Implement pop_front - remove and return the item at the front of the deque
        :return: int
        """

        popped_item = self.front()
        self.list.delete(popped_item)

        return popped_item

    def pop_back(self):
        """
        Implement pop_back - remove and return the item at the back of the deque
        :return: int
        """

        popped_item = self.back()
        self.list.delete(popped_item)

        return popped_item

