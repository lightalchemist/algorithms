#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: queue.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Implementation of a queue using an array.
Array is dynamically resized when necessary.

Note that although Python's list can essentially function as a queue,
we ignore those features and use it simply as a normal array.
Hence, this implementation is just for self-study and not
a practical one.
"""

from rotate_array import rotate

class Queue(object):

    def __init__(self, capacity):
        self._count = 0
        self._head = 0
        self._tail = 0
        self._array = [None] * capacity


    def enqueue(self, item):
        # Resize array
        if self._count == len(self._array):
            rotate(self._array, 0, self._head, len(self._array))  # Move head to front
            self._head = 0
            self._tail = self._count
            self._array += [None] * len(self._array)  # Double capacity

        self._array[self._tail] = item
        self._tail = (self._tail + 1) % len(self._array)
        self._count += 1


    def dequeue(self):
        if self._count == 0:
            raise IndexError("Cannot dequeue an empty queue.")

        item = self._array[self._head]
        self._count -= 1
        self._head = (self._head + 1) % len(self._array)
        return item


    def __len__(self):
        return self._count


    def __str__(self):
        s = [self._array[(self._head + i) % len(self._array)]  for i in range(self._count)]
        return str(s)


def test():
    q = Queue(10)
    assert len(q) == 0

    q.enqueue(1)
    assert len(q) == 1

    q.enqueue(2)
    assert len(q) == 2

    v = q.dequeue()
    assert v == 1
    assert len(q) == 1

    v = q.dequeue()
    assert v == 2
    assert len(q) == 0

    q = Queue(10)
    for i in range(10):
        q.enqueue(i)
    assert len(q) == 10
    q.enqueue(10)
    assert len(q) == 11
    assert str(q) == str(range(11))

    q = Queue(10)
    for i in range(10):
        q.enqueue(i)
    assert len(q) == 10
    assert q.dequeue() == 0
    assert q.dequeue() == 1
    assert len(q) == 8
    q.enqueue(10)
    q.enqueue(11)
    q.enqueue(12)
    assert str(q) == str(list(range(2, 13)))


    print("All tests pass.")


if __name__ == '__main__':
    test()
