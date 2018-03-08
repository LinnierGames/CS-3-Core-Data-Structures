#!python

from hashset import HashSet


class Set(HashSet):

    def __init__(self, elements=None):
        super(Set, self).__init__(elements)

    def union(self, other_set):
        return Set(self.items() + other_set.items())

    def intersection(self, other_set):
        self_items = self.items()
        other_items = other_set.items()

        return [intersection for intersection in self_items if intersection in other_items]