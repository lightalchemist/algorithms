#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
File: queue_using_stacks.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Implementing a queue from 2 stacks.

Enqueue and dequeue takes O(n) time amortized over n enqueue and dequeue.

This is a contrived implementation of a queue and is done simply for pedagogical reasons.
"""

from stack import Stack


class Queue(object):

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()


    def enqueue(self, item):
        self.s1.push(item)


    def dequeue(self):
        """When dequeuing, if stack s2 is empty, we push everthing from s1 onto it.
        Now, s2 will be able to pop the values in FIFO order.
        For enqueuing, we continue to push onto s1 and push everything from s2 when necessary
        (i.e., when s2 is once again empty).
        """
        if not self.s2.empty():
            return self.s2.pop()
        else:
            while not self.s1.empty():
                self.s2.push(self.s1.pop())

            return self.s2.pop()


    def __len__(self):
        return len(self.s1) + len(self.s2)


    def __str__(self):
        values = [node.value[0] for node in self.s2]
        values += reversed([node.value[0] for node in self.s1])
        return str(values)


def test():
    q = Queue()
    q.enqueue(1)

    assert len(q) == 1
    assert str(q) == "[1]"

    v = q.dequeue()
    assert v == 1
    assert len(q) == 0

    for i in range(5):
        q.enqueue(i)
    assert len(q) == 5
    v = q.dequeue()
    assert v == 0
    v = q.dequeue()
    assert v == 1
    v = q.dequeue()
    assert v == 2
    q.enqueue(5)
    assert len(q) == 3
    v = q.dequeue()
    assert v == 3
    q.enqueue(6)
    assert len(q) == 3
    v = q.dequeue()
    assert v == 4

    assert str(q) == "[5, 6]"

    print("All tests pass.")


if __name__ == '__main__':
    test()
