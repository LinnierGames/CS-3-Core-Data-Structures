#!python

from hashset import HashSet


class Set(HashSet):

    def __init__(self, elements=None):
        super(Set, self).__init__(elements)