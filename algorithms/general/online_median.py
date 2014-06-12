#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: online_median.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Compute running median in O(log n) time using O(n) space.

Sequence is giving in streaming manner one at a time.
The MedianTracker code presented here allows the median to be computed
in O(log n) time when requested after a series of updates.

"""

from heapq import heappush
from heapq import heappop


class MedianTracker(object):

    def __init__(self):
        self._min_heap = []
        self._max_heap = []


    def update(self, x):
        """Update median tracker with number x."""
        # Note that we implement max heap using a min heap by pre-multiplying
        # number by -1 before insertion and multiplying by -1 after popping.
        if len(self._min_heap) > len(self._max_heap):
            if x > self._min_heap[0]:
                y =  heappop(self._min_heap)
                heappush(self._max_heap, -y)
                heappush(self._min_heap, x)
            else:
                heappush(self._max_heap, -x)
        elif len(self._min_heap) < len(self._max_heap):
            if x > (-self._max_heap[0]):
                heappush(self._min_heap, x)
            else:
                y = - heappop(self._max_heap)
                heappush(self._max_heap, -x)
                heappush(self._min_heap, y)
        else:  # Same number of items on each heap.
            if len(self._min_heap) == 0:  # Both heaps empty. Doesn't matter which we add to.
                heappush(self._min_heap, x)
            elif x <= - (self._max_heap[0]):  # Smaller than largest of smaller half
                heappush(self._max_heap, -x)
            else:
                heappush(self._min_heap, x)


    def get_median(self):
        if (len(self._min_heap) + len(self._max_heap)) % 2 == 0:
            return (self._min_heap[0] + (-self._max_heap[0])) / 2.0
        elif len(self._min_heap) > len(self._max_heap):
            return self._min_heap[0]
        else:
            return -self._max_heap[0]


    def __len__(self):
        return len(self._min_heap) + len(self._max_heap)


def test():
    import random
    import numpy as np
    tracker = MedianTracker()
    # Generate random sequence of 30 numbers
    s = [random.randint(-100, 100) for _ in range(100)]
    # Update median tracker one number at a time and check against
    # actual median computed from actual sequence up to that number
    for i, x in enumerate(s):
        tracker.update(x)
        assert tracker.get_median() == np.median(s[:i+1])

    tracker = MedianTracker()
    tracker.update(1)
    m = tracker.get_median()
    assert m == 1

    tracker.update(2)
    assert len(tracker) == 2
    assert tracker.get_median() == 1.5

    tracker.update(2)
    assert tracker.get_median() == 2
    assert len(tracker) == 3

    print("All tests pass.")


if __name__ == '__main__':
    test()
