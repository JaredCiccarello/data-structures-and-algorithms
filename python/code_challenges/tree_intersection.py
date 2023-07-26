from data_structures.binary_tree import BinaryTree
from data_structures import hashtable

def tree_intersection(tree1, tree2):
    values_set1 = set()
    values_set2 = set()

    # In order to traverse the binary tree and add values
    def traverse_tree(node, values_set):
        if not node:
            return
        values_set.add(node.value)  # Assuming the node has a 'value' attribute
        traverse_tree(node.left, values_set)
        traverse_tree(node.right, values_set)

    # Traverse the first tree and add its values to the set
    traverse_tree(tree1.root, values_set1)  # Assuming the root of the tree is accessible through the 'root' attribute

    # Traverse the second tree and add its values to the set
    traverse_tree(tree2.root, values_set2)  # Assuming the root of the tree is accessible through the 'root' attribute

    # Find the intersection of the two sets (values common in both trees)
    common_values = values_set1.intersection(values_set2)

    return common_values


