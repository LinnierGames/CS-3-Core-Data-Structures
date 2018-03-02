#!python

from deque import LinkedDeque
import unittest


class QueueTest(unittest.TestCase):

    def test_init(self):
        q = LinkedDeque()
        assert q.front() is None
        assert q.length() == 0
        assert q.is_empty() is True

    def test_front(self):
        q = LinkedDeque()
        assert q.front() is None

    def test_back(self):
        q = LinkedDeque()
        assert q.back() is None

    def test_push_front(self):
        q = LinkedDeque()
        q.push_front("A")
        assert q.length() == 1
        q.push_front("B")
        assert q.length() == 2
        assert q.front() == "B"
        assert q.back() == "A"

    def test_push_back(self):
        q = LinkedDeque()
        q.push_back("A")
        assert q.length() == 1
        q.push_back("B")
        assert q.length() == 2
        assert q.front() == "A"
        assert q.back() == "B"

    def test_pop_back(self):
        q = LinkedDeque()
        with self.assertRaises(ValueError):
            q.pop_back()
        q.push_front("A")
        assert q.length() == 1
        assert q.pop_back() == "A"
        assert q.is_empty() is True
        q.push_back("two")
        q.push_front("one")
        assert q.pop_back() == "two"
        assert q.pop_back() == "one"
        with self.assertRaises(ValueError):
            q.pop_back()
        assert q.is_empty() is True

    def test_pop_front(self):
        q = LinkedDeque()
        with self.assertRaises(ValueError):
            q.pop_front()
        q.push_front("A")
        assert q.length() == 1
        assert q.pop_front() == "A"
        assert q.is_empty() is True
        q.push_front("one")
        q.push_back("two")
        assert q.pop_front() == "one"
        assert q.pop_front() == "two"
        with self.assertRaises(ValueError):
            q.pop_front()
        assert q.is_empty() is True


if __name__ == '__main__':
    unittest.main()
