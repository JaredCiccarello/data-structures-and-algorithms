import pytest
from data_structures.binary_tree import BinaryTree, Node


# @pytest.mark.skip("TODO")
def test_max_val():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)

    actual = tree.find_maximum_value()
    expected = 30

    assert actual == expected

def test_max_val_empty():
    tree = BinaryTree()
    actual = tree.find_maximum_value()
    expected = None
    assert actual == expected

def test_max_val_single_node():
    tree = BinaryTree(Node(10))
    actual = tree.find_maximum_value()
    expected = 10
    assert actual == expected

def test_max_val_negative_values():
    tree = BinaryTree(Node(-5))
    tree.root.left = Node(-10)
    tree.root.right = Node(-3)
    tree.root.left.left = Node(-2)
    tree.root.left.right = Node(-7)
    tree.root.right.right = Node(-1)
    actual = tree.find_maximum_value()
    expected = -1
    assert actual == expected
