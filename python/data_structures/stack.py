import pytest
from data_structures.invalid_operation_error import InvalidOperationError
# from node import Node


class Stack:
    """
    Create a Stack class that has a top property. It creates an empty Stack when instantiated.
    This object should be aware of a default empty value assigned to top when the stack is created.
    """

    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")

        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")

        return self.top.value

    def is_empty(self):
        return self.top is None


def test_exists():
    assert Stack


def test_push_onto_empty():
    s = Stack()
    s.push("apple")
    actual = s.top.value
    expected = "apple"
    assert actual == expected


class Node:

    # The constructor initializes a node with the given value.

    def __init__(self, value):
        self.value = value
        self.next = None
