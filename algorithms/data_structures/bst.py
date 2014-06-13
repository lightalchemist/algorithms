#!/usr/bin/env python
# -*- coding: utf-8 -*-


class bst(object):

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def insert(T, data):
    """Insert data into a bst while maintaining the bst property."""
    if data <= T.data:
        if T.left is None:  # Add sub-tree to hold data
            T.left = bst(data)
        else:
            insert(T.left, data)  # Recursively add into left tree
    else:
        if T.right is None:
            T.right = bst(data)
        else:
            insert(T.right, data)


def check_bst_property(T):
    """Check the BST property of a bst."""
    left_result = right_result = True
    if T.left:
        left_result = check_bst_property(T.left) and T.data >= T.left.data
    if T.right:
        right_result = check_bst_property(T.right) and T.data < T.right.data

    return left_result and right_result


def inorder_traversal(T, order=None):
    """Traverse a bst in inorder.
    Return the order of item encountered.
    """
    if T is None:
        return

    if order is None:
        order = []

    inorder_traversal(T.left, order)
    order.append(T.data)
    inorder_traversal(T.right, order)


def preorder_traversal(T):
    """Traverse a bst in preorder.
    Return the order of item encountered.
    """
    if T is None:
        return

    print(T.data)
    preorder_traversal(T.left)
    preorder_traversal(T.right)


def postorder_traversal(T):
    """Traverse a bst in postorder.
    Return the order of item encountered.
    """
    if T is None:
        return

    preorder_traversal(T.left)
    preorder_traversal(T.right)
    print(T.data)


def test():
    b = bst()
    b.data = 5

    left = bst(2)
    right = bst(6)
    b.left = left
    b.right = right
    result = []
    inorder_traversal(b, result)
    assert result == [2, 5, 6]
    assert check_bst_property(b)

    b = bst()
    assert check_bst_property(b)

    b.data = 1
    left = bst(-1)
    right = bst(-2)
    b.left = left
    b.right = right
    assert check_bst_property(b) == False

    b = bst(5)
    insert(b, 1)
    insert(b, 6)
    insert(b, 10)
    insert(b, 2)
    result = []
    inorder_traversal(b, result)
    assert result == [1, 2, 5, 6, 10]
    assert check_bst_property(b)


if __name__ == '__main__':
    test()
