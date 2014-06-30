#!/usr/bin/env python


def sort(a):
    for i in range(1, len(a)):
        j = i
        # Swap element i all the way to position 0 if necessary
        while j > 0 and a[j] < a[j - 1]:
            a[j - 1], a[j] = a[j], a[j - 1]
            j -= 1


import copy
import random

def test():
    a = range(10)
    random.shuffle(a)
    b = copy.copy(a)
    sort(a)
    assert a == sorted(b)

    a = [1, 1, 1, 1]
    sort(a)
    assert a == [1, 1, 1, 1]

    a = [-1]
    sort(a)
    assert a == [-1]

    a = [random.randint(-100, 100) for _ in range(100)]
    b = copy.copy(a)
    sort(a)
    assert a == sorted(b)


if __name__ == '__test__':
    test()
