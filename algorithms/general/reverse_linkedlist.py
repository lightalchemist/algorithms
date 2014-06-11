#!/usr/bin/env python
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    import sys
    sys.path.insert(0, "..")


from data_structures.linked_list import LinkedList


def reverse(linkedlist):
    """Reverse a linked list in O(n) time using O(1) storage."""
    before = None
    current = linkedlist.head
    while current is not None:
        linkedlist._head = current  # Move head to current node
        after = current.next_element
        current.next_element = before  # Reverse pointer
        before = current  # Move pointers 1 step
        current = after


def test():
    a = LinkedList()
    reverse(a)
    assert str(a) == "[]"

    a = LinkedList([2])
    reverse(a)
    assert str(a) == "[2]"

    a = LinkedList([1, 2, 3])
    reverse(a)
    assert str(a) == "[3, 2, 1]"

    a = LinkedList(range(10))
    reverse(a)
    assert str(a) == str(list(reversed(range(10))))


if __name__ == '__main__':
    test()
