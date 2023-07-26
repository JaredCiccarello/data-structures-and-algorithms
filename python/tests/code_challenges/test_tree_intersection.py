import pytest
from code_challenges.tree_intersection import tree_intersection
from data_structures.binary_tree import BinaryTree, Node
from data_structures.queue import Queue


def test_exists():
    assert tree_intersection


# @pytest.mark.skip("TODO")
def test_tree_intersection():

    tree_a = BinaryTree()
    values = [150, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500]
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = [42, 100, 100, 15, 160, 200, 350, 125, 175, 4, 500]
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    expected = [125, 175, 100, 160, 500, 200, 350]

    assert sorted(actual) == sorted(expected)


def add_values_to_empty_tree(tree, values):
    """
    Helper function to add given values to BinaryTree
    """
    tree.root = Node(values.pop())
    q = Queue()

    q.enqueue(tree.root)

    while values:
        node = q.dequeue()
        node.left = Node(values.pop())
        node.right = Node(values.pop()) if values else None
        q.enqueue(node.left)
        q.enqueue(node.right)

def test_tree_intersection_with_multiple_common_values():
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)
    root1.right.right = Node(6)

    root2 = Node(2)
    root2.left = Node(3)
    root2.right = Node(1)
    root2.left.left = Node(5)
    root2.left.right = Node(6)
    root2.right.right = Node(2)

    tree1 = BinaryTree(root1)
    tree2 = BinaryTree(root2)

    actual = tree_intersection(tree1, tree2)
    expected = {1, 2, 3, 5, 6}

    assert actual == expected


def test_tree_intersection_with_some_common_values():
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)
    root1.right.right = Node(6)

    root2 = Node(2)
    root2.left = Node(3)
    root2.right = Node(1)
    root2.left.left = Node(5)
    root2.left.right = Node(6)
    root2.right.right = Node(2)

    tree1 = BinaryTree(root1)
    tree2 = BinaryTree(root2)

    actual = tree_intersection(tree1, tree2)
    expected = {1, 2, 3, 5, 6}

    assert actual == expected
