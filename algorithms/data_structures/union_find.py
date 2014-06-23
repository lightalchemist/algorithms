#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: union_find.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Union-Find data structure for quickly
checking if 2 nodes p, q, are connected.

Time complexity to check if p, q are connected: O(logn)
Time complexity to connect node p and q: O(logn)

"""

class UnionFindBasic(object):

    def __init__(self, num_elements):
        """Initialize union find data structure for num_elements."""
        self._id = range(num_elements)


    def find(self, p):
        """Return the root of node p,
        which is also the id of the connected component p belongs to."""
        return self._id[p]


    def is_connected(self, p, q):
        """Return true if 2 nodes p, q, are connected, else False."""
        return self.find(p) == self.find(q)


    def union(self, p, q):
        """Connect node q and node q."""
        newfind = self._id[p]
        oldfind = self._id[q]
        for i, x in enumerate(self._id):
            if x == oldfind:
                self._id[i] = newfind


    def reset(self):
        """Reset data structure to state when it was just initialized."""
        self._id = range(len(self._id))


    def __len__(self):
        return len(self._id)


    def __str__(self):
        return "Union-Find for {} elements.".format(len(self))


class UnionFindWeighted(UnionFindBasic):

    def __init__(self, num_elements):
        super(UnionFindWeighted, self).__init__(num_elements)
        self._num_elements = num_elements
        self._size = [0] * num_elements  # For tracking size of each subtree


    def find(self, p):
        """Return the root of node p,
        which is also the id of the connected component p belongs to."""
        i = p
        while i != self._id[i]:  # Root node is node that points to itself
            i = self._id[i]

        return i


    def union(self, p, q):
        """Connect node q and node q."""
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p != root_q:
            if self._size[root_p] < self._size[root_q]:
                # Connect subtree containing p to root of q
                self._size[root_q] += self._size[root_p]
                self._id[root_p] = root_q
            else:
                # Connect subtree containing q to root of p
                self._size[root_p] += self._size[root_q]
                self._id[root_q] = root_p


    def reset(self):
        """Reset data structure to state when it was just initialized."""
        super(UnionFindWeighted, self).reset()
        self._size = [0] * self._num_elements


    def __str__(self):
        return "Union-Find with weighting for {} elements.".format(len(self))


class UnionFindWithPathCompression(UnionFindWeighted):

    def __init__(self, num_elements):
        super(UnionFindWithPathCompression, self).__init__(num_elements)


    def find(self, p):
        i = p
        while i != self._id[i]:
            self._id[i] = self._id[self._id[i]]  # Path compression.
            i = self._id[i]

        return i


    def __str__(self):
        return "Union-Find with weighting and path compression for "\
                "{} elements.".format(len(self))


def test():
    n = 10000
    for uf in (UnionFindBasic(n), UnionFindWeighted(n), UnionFindWithPathCompression(n)):
        print("Testing : {}".format(uf))
        test_uf(uf)

    print("All tests pass")


def test_uf(uf):

    uf.union(0, 1)
    assert uf.is_connected(0, 1) == True
    assert uf.is_connected(0, 2) == False
    assert uf.is_connected(1, 2) == False

    uf.union(2, 3)
    assert uf.is_connected(2, 3) == True
    assert uf.is_connected(0, 2) == False
    assert uf.is_connected(0, 3) == False
    assert uf.is_connected(1, 2) == False
    assert uf.is_connected(1, 3) == False

    uf.union(1, 3)
    assert uf.is_connected(0, 2) == True
    assert uf.is_connected(0, 3) == True
    assert uf.is_connected(1, 2) == True
    assert uf.is_connected(1, 3) == True

    uf.union(7, 9)
    assert uf.is_connected(0, 7) == False
    assert uf.is_connected(0, 9) == False
    assert uf.is_connected(1, 7) == False

    uf.union(5, 8)
    assert uf.is_connected(0, 8) == False
    assert uf.is_connected(1, 5) == False
    assert uf.is_connected(2, 7) == False

    uf.union(4, 8)
    assert uf.is_connected(5, 7) == False
    assert uf.is_connected(8, 9) == False
    assert uf.is_connected(0, 7) == False
    assert uf.is_connected(1, 7) == False
    assert uf.is_connected(2, 7) == False
    assert uf.is_connected(3, 7) == False

    uf.union(2, 8)
    for i in range(6):
        assert uf.is_connected(i, 8) == True
        assert uf.is_connected(i, 7) == False
        assert uf.is_connected(i, 9) == False
        assert uf.is_connected(i, 6) == False

    for i in range(6):
        for j in range(i, 6):
            assert uf.is_connected(i, j) == True

    uf.union(9, 0)
    for i in range(10):
        for j in range(10):
            if (j == 6 or i == 6) and i != j:
                assert uf.is_connected(i,  j) == False
            else:
                assert uf.is_connected(i,  j) == True

    uf.reset()
    assert uf.is_connected(0, 1) == False

    uf.union(0, 1)
    uf.union(2, 3)
    uf.union(4, 5)
    uf.union(6, 7)
    uf.union(0, 3)
    uf.union(4, 6)
    uf.union(0, 7)

    uf.union(8, 9)
    uf.union(8, 5)

    for i in range(10):
        for j in range(10):
            assert uf.is_connected(i, j) == True


if __name__ == "__main__":
    test()
