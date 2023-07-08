from data_structures.binary_tree import BinaryTree

# class BinaryTree:
#       def __init__(self, root=None):
#         self.root = root

def breadth_first(tree):
    arr = []
    if tree.root is None:
        return arr

    queue = []
    queue.append(tree.root)

    while queue:
        node = queue.pop(0)
        arr.append(node.value)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return arr
