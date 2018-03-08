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

    def difference(self, other_set):
        self_items = self.items()
        other_items = other_set.items()

        for an_item in other_items:
            if an_item in self_items:
                self_items.remove(an_item)

        return self_items
