#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: k_smallest_in_file.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Given a large file that we cannot fit into memory,
we wish to extract the lines that has the k smallest values
with the value of each line computed using a given key operator.
"""

import itertools
from heapq import heappush
from heapq import heappop


def find_k_smallest(filename, k, key):
    heap = []
    with open(filename) as infile:
        for line in itertools.islice(infile, 0, k):
            heappush(heap, (-key(line), line))

        for line in infile:
            v = key(line)
            if v < (-heap[0][0]):  # Smaller than largest of k smallest numbers
                heappop(heap)
                heappush(heap, (-v, line))

    k_smallest = [heappop(heap)[1] for _ in range(k)]
    # If order does not matter, then the list is just the unraveled heap.
    # k_smallest = [x[1] for x in heap]
    return k_smallest


def test():
    test_filename = "test_k_smallest.txt"
    k = 3
    key = lambda line: int(line.split(',')[0])
    k_smallest = find_k_smallest(test_filename, k, key)
    assert k_smallest == ["3,item4\n", "2,item6\n", "-1,item3\n"]


if __name__ == '__main__':
    test()
