#!/usr/bin/env python


def swim(arr, i):
    # Swim item at n - 1 as far up as necessary
    while i > 1 and arr[i // 2] < arr[i]:
        arr[i // 2], arr[i] = arr[i], arr[i // 2]
        i = i // 2


def sink(arr, i):
    n = len(arr) - 1
    while 2 * i <= n:
        j = 2 * i
        if j < n and arr[j] < arr[j + 1]:  # Point j to larger of 2 child
            j += 1

        if arr[i] >= arr[j]:  # Position already correct
            break

        arr[i], arr[j] = arr[j], arr[i]
        i = j


def heapify(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        swim(arr, i)


def heappop(arr):
    item = arr[1]
    n = len(arr) - 1
    arr[1], arr[n] = arr[n], arr[1]
    arr.pop()
    sink(arr, 1)

    return item


def heappush(arr, item):
    n = len(arr)
    arr.append(item)
    swim(arr, n)


def heapsort(arr):
    n = len(arr)
    arr = [-1] + arr
    heapify(arr)
    return [heappop(arr) for i in range(n)]


import random


def main():
    arr = [-1, 1, 2, 3]
    sink(arr, 1)
    assert arr == [-1, 3, 2, 1]

    arr = [-1, 1, 2, 3]
    swim(arr, 3)
    assert arr == [-1, 3, 2, 1]

    arr = [-1, 1, 2, 3]
    heapify(arr)
    assert arr == [-1, 3, 2, 1]

    arr = range(10)
    random.shuffle(arr)
    print("shuffled array: {}".format(arr))
    sorted_arr = heapsort(arr)
    print(sorted_arr)
    # assert arr == range(10)


    print("All tests pass")


if __name__ == '__main__':
    main()
