#!python

from set import Set
import unittest


class HashSetTest(unittest.TestCase):

    def test_init(self):
        set = Set(['A','B','C'])
        assert len(set) == 3
        assert set.contains('A') is True
        assert set.contains('B') is True
        assert set.contains('C') is True

    def test_add_remove(self):
        set = Set()
        set.add('A')
        assert len(set) == 1
        assert set.contains('A') is True
        set.add('B')
        assert len(set) == 2
        assert set.contains('B') is True
        set.add('C')
        assert len(set) == 3
        assert set.contains('C') is True
        set.remove('B')
        assert len(set) == 2
        assert set.contains('B') is False
        set.remove('A')
        assert len(set) == 1
        assert set.contains('A') is False
        set.remove('C')
        assert len(set) == 0
        assert set.contains('C') is False
        with self.assertRaises(ValueError):
            set.remove('C')



if __name__ == '__main__':
    unittest.main()
