#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: kth_largest_element.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description:  Output the kth largest numbers we've seen so far from a stream.

We maintain a heap of k largest numbers we've encountered so far.
When we get a new number, we check if it is > the smallest of these k numbers.
If so, we remove the smallest number in the heap and add this number as one of the
k largest numbers we've seen so far.
Lastly, we return the minimum element of the heap,
which is also the kth largest number encountered so far.

In the event that we have not seen k numbers yet, we just output the minimum
element encountered so far.
"""

from heapq import heappush
from heapq import heappop


def output_kth_largest(stream, k):
    heap = []
    for item in stream:
        if len(heap) == k:
            # Replace current kth largest with new item if
            # new item is one of the kth largest now.
            if item > heap[0]:
                heappop(heap)
                heappush(heap, item)
        else:
            heappush(heap, item)

        # Return smallest number in heap of k largest numbers seen so far
        yield heap[0]


def test():
    stream = [2, 1, 3, 4, 5]
    kth_largest_seq = [x for x in output_kth_largest(stream, 2)]
    assert kth_largest_seq == [2, 1, 2, 3, 4]

    stream = [2, 1, 3, -1, 1, 5]
    kth_largest_seq = [x for x in output_kth_largest(stream, 2)]
    assert kth_largest_seq == [2, 1, 2, 2, 2, 3]

    stream = [-1, -1, -1]
    kth_largest_seq = [x for x in output_kth_largest(stream, 2)]
    assert kth_largest_seq == [-1, -1, -1]

    stream = [-1, 0, -1]
    kth_largest_seq = [x for x in output_kth_largest(stream, 2)]
    assert kth_largest_seq == [-1, -1, -1]

    stream = [-1, 0, -1]
    kth_largest_seq = [x for x in output_kth_largest(stream, 2)]
    assert kth_largest_seq == [-1, -1, -1]

if __name__ == '__main__':
    test()
