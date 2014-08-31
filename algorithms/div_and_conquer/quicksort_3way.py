#!/usr/bin/env python

import random


def quicksort(arr):
    random.shuffle(arr)  # Random shuffle to avoid degenerate cases leading to O(n^2) runtime
    quicksort_helper(arr, 0, len(arr) - 1)
    return arr


def quicksort_helper(arr, lo, hi):
    if hi <= lo:
        return;

    # 3 way partitioning invariants:
    # arr[lo:lt] < pivot
    # arr[lt:i] == pivot
    # arr[gt+1:] > pivot
    # arr[i:gt] unclassified
    i = lt = lo
    gt = hi
    pivot = arr[lo]
    while i <= gt:
        if arr[i] < pivot:
            arr[i], arr[lt] = arr[lt], arr[i]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:  # arr[i] == pivot
            i += 1

    quicksort_helper(arr, lo, lt-1)
    quicksort_helper(arr, gt + 1, hi)


def test():
    s = [-1]
    s_sorted = quicksort(s)
    assert s_sorted == sorted(s)

    s = []
    s_sorted = quicksort(s)
    assert s_sorted == sorted(s)

    s = [2, -1]
    s_sorted = quicksort(s)
    assert s_sorted == sorted(s)

    s = [random.randint(-100, 100) for _ in range(10000)]
    s_sorted = quicksort(s)
    assert s_sorted == sorted(s)


if __name__ == '__main__':
    test()
