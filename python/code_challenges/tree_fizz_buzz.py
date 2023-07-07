# from data_structures.binary_tree import BinaryTree
# from data_structures.binary_tree import Node

# def fizz_buzz_tree(tree):
#     if tree.root is None:
#         return BinaryTree()

#     def fizz_buzz_value(value):
#         if value % 3 == 0 and value % 5 == 0:
#             return "FizzBuzz"
#         elif value % 3 == 0:
#             return "Fizz"
#         elif value % 5 == 0:
#             return "Buzz"
#         else:
#             return str(value)

#     def traverse(node):
#         if node is None:
#             return None

#         fizz_buzzed_node = Node(fizz_buzz_value(node.value))

#         fizz_buzzed_node.left = traverse(node.left)
#         fizz_buzzed_node.right = traverse(node.right)

#         return fizz_buzzed_node

#     fizz_buzzed_tree = BinaryTree(traverse(tree.root))
#     return fizz_buzzed_tree

from data_structures.binary_tree import BinaryTree
from data_structures.kary_tree import KaryTree, Node


class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.children = []

def fizz_buzz_tree(tree):
    if not tree.root:
        return None

    new_tree = KaryTree(TreeNode(None))  # Create a new KaryTree with the modified TreeNode
    process_node(tree.root, new_tree.root)  # Pass the root nodes to process

    return new_tree

def process_node(current_node, new_node):
    if current_node.value % 3 == 0 and current_node.value % 5 == 0:
        new_node.value = "FizzBuzz"
    elif current_node.value % 3 == 0:
        new_node.value = "Fizz"
    elif current_node.value % 5 == 0:
        new_node.value = "Buzz"
    else:
        new_node.value = str(current_node.value)

    for child_node in current_node.children:
        new_child_node = TreeNode(None)
        new_node.children.append(new_child_node)
        process_node(child_node, new_child_node)
