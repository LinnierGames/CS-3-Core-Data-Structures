#!python

from linkedlist import LinkedList


class HashSet(object):

    def __init__(self, elements=None):
        """Initialize this hash table with the given initial size."""
        init_size = 8
        self.buckets = [LinkedList() for i in range(init_size)]
        self.size = 0  # Number of key-value entries

        if elements is not None:
            for an_element in elements:
                self.add(an_element)

    def __str__(self):
        """Return a formatted string representation of this hash table."""

        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""

        return 'HashTable({!r})'.format(self.items())

    def __len__(self):
        return self.size

    def _bucket_index(self, element):
        """Return the bucket index where the given key would be stored."""
        return hash(element) % len(self.buckets)

    def load_factor(self):
        """Return the load factor, the ratio of number of entries to buckets.
        Best and worst case running time: ??? under what conditions? [TODO]"""

        entries = self.size
        buckets = len(self.buckets)

        # floating point division
        return float(entries) / float(buckets) if buckets != 0 else 0

    def items(self):
        """Return a list of all keys in this hash table.
        Best and worst case running time: ??? under what conditions? [TODO]"""

        # Collect all keys in each of the buckets
        all_elements = []
        for bucket in self.buckets:
            for an_element in bucket.items():
                all_elements.append(an_element)

        return all_elements

    def contains(self, element):
        """Return True if this hash table contains the given key, or False.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""

        # Find the bucket the given key belongs in
        index = self._bucket_index(element)
        bucket = self.buckets[index]

        # Check if an entry with the given key exists in that bucket
        found_element = bucket.find(lambda an_element: an_element == element)

        # True or False
        return found_element is not None

    def add(self, element):
        """Insert or update the given key with its associated value.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""

        # Find the bucket the given key belongs in
        index = self._bucket_index(element)
        bucket = self.buckets[index]

        # Find the entry with the given key in that bucket, if one exists
        # Check if an entry with the given key exists in that bucket
        found_element = bucket.find(lambda an_element: an_element == element)
        if found_element is None:  # Not Found

            # Insert the new key-value entry into the bucket in either case
            bucket.append(element)
            self.size += 1

            # check load factory
            if self.load_factor() > 0.75:
                self._resize()

    def remove(self, element):
        """Delete the given key and its associated value, or raise KeyError.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""

        # Find the bucket the given key belongs in
        index = self._bucket_index(element)
        bucket = self.buckets[index]

        # Find the entry with the given key in that bucket, if one exists
        found_element = bucket.find(lambda an_element: an_element == element)
        if found_element is not None:  # Found

            # Remove the key-value entry from the bucket
            bucket.delete(found_element)
            self.size -= 1

        else:  # Not found
            raise ValueError('Key not found: {}'.format(found_element))

    def _resize(self, new_size=None):
        """Resize this hash table's buckets and rehash all key-value entries.
        Should be called automatically when load factor exceeds a threshold
        such as 0.75 after an insertion (when set is called with a new key).
        Best and worst case running time: ??? under what conditions? [TODO]
        Best and worst case space usage: ??? what uses this memory? [TODO]"""

        # If unspecified, choose new size dynamically based on current size
        if new_size is None:
            new_size = len(self.buckets) * 2  # Double size

        # Option to reduce size if buckets are sparsely filled (low load factor)
        elif new_size is 0:
            new_size = len(self.buckets) / 2  # Half size

        # store the items to be transferred
        to_be_transferred = self.items()

        # reset the hash table
        self.buckets = [LinkedList() for i in range(new_size)]
        self.size = 0

        for an_element in to_be_transferred:

            # insert the transferred items to their new buckets
            self.add(an_element)


def test_hash_table():
    ht = HashTable(4)
    print('HashTable: ' + str(ht))

    print('Setting entries:')
    ht.set('I', 1)
    print('set(I, 1): ' + str(ht))
    ht.set('V', 5)
    print('set(V, 5): ' + str(ht))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))
    ht.set('X', 10)
    print('set(X, 10): ' + str(ht))
    ht.set('L', 50)  # Should trigger resize
    print('set(L, 50): ' + str(ht))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))

    print('Getting entries:')
    print('get(I): ' + str(ht.get('I')))
    print('get(V): ' + str(ht.get('V')))
    print('get(X): ' + str(ht.get('X')))
    print('get(L): ' + str(ht.get('L')))
    print('contains(X): ' + str(ht.contains('X')))
    print('contains(Z): ' + str(ht.contains('Z')))

    print('Deleting entries:')
    ht.delete('I')
    print('delete(I): ' + str(ht))
    ht.delete('V')
    print('delete(V): ' + str(ht))
    ht.delete('X')
    print('delete(X): ' + str(ht))
    ht.delete('L')
    print('delete(L): ' + str(ht))
    print('contains(X): ' + str(ht.contains('X')))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))


if __name__ == '__main__':
    test_hash_table()
