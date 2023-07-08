from data_structures.binary_tree import BinaryTree
from data_structures.binary_tree import Node

class BinarySearchTree(BinaryTree):
    """
    provide operations to create, manipulate, and search a binary search tree.
    """
    def __init__(self, root=None):
      self.root = root

    def __init__(self):
        # initialization here
        super().__init__()
        self.root = None
        self.Node = Node

    def add(self, value):
      """
      Adds a new node with the given value to the binary search tree.
      """
      if self.root is None:
            self.root = Node(value)
      else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, node, value):
        """
        Helper method for recursive insertion of a node.
        """
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add_recursive(node.right, value)

    def contains(self, value):
        """
        Checks if the binary search tree contains a node with the given value.
        Returns True if found, False otherwise.
        """
        return self._contains_recursive(self.root, value)

    def _contains_recursive(self, node, value):
        """
        Helper method for recursive search of a value in the binary search tree.
        """
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._contains_recursive(node.left, value)
        else:
            return self._contains_recursive(node.right, value)
