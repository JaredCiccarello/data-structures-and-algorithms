class BinaryTree:
    def __init__(self, root=None):
        self.root = root
    """
    Put docstring here
    """

    def pre_order(self, values=[]):
        def walk(input_node, value_list):
            if not input_node:
                return
            value_list.append(input_node.value)
            walk(input_node.left, value_list)
            walk(input_node.right, value_list)

        walk(self.root, values)
        return values

    def in_order(self, values=[]):
        def walk(input_node, value_list):
            if not input_node:
                return
            walk(input_node.left, value_list)
            value_list.append(input_node.value)
            walk(input_node.right, value_list)

        walk(self.root, values)
        return values

    def post_order(self, values=[]):
        def walk(input_node, value_list):
            if not input_node:
                return
            walk(input_node.left, value_list)
            walk(input_node.right, value_list)
            value_list.append(input_node.value)

        walk(self.root, values)
        return values


    # def find_maximum_value(self):
    #     if self.root is None:
    #         return None

    #     max_value = -1
    #     node = self.root
    #     while node:
    #         if node.value > max_value:
    #             max_value = node.value
    #             node = node.left

    #     return max_value

    def find_maximum_value(self):
        if self.root is None:
            return None

        def traverse(node):
            if node is None:
                # inf stands for negativity infinity.
                # this allows 
                return float('-inf')

            left_max = traverse(node.left)
            right_max = traverse(node.right)

            return max(node.value, left_max, right_max)

        return traverse(self.root)

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

