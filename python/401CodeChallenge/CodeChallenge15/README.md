Collaborators
Andrew Carroll
Anthony Sinitsa
Logan Reese
Sarah Glass
Slava Makeev

# Challenge Title
Code Challenge: Class 15

## Whiteboard Process
No Whiteboard

## Approach & Efficiency
Time: o(n)
Space: o(n)

## Solution
run pytest
python/code_challenges/test_binary_tree.py
python/code_challenges/test_binary_tree_search.py

Datastructure: BinaryTree, BinarySearchTree

In a Node, you have two children: your left and your right child Nodes.

The role of a BinaryTree is to create methods in order to traverse and manipulate through the binarySearchTree.
BinaryTree:
First you'll need to initialize a binary tree with an optional root node.
Then create the functions: Pre_order, in_order, Post_order, and max_value
These methods to traverse a binary tree to return a list of values in the order they are visited.
Max_value traverses through each node, comparing the highest value to the current value. Once it has traversed through all the nodes, it will return the value that it is currently assigned. Which will be the highest value compared to each Node.

The purpose of the BinarySearchTree class is to provide operations to create, manipulate, and search a binary search tree.
It allows for adding nodes to the binary search tree and searching for values within the tree.

BinarySearchTree:
 Initializes a binarySearchTree with an optional root node.
 The Add function adds a new node with the given value to the binary search tree.
_add_recursive function is used for recursive insertion of a node in the binary search tree.
contains function Checks if the binary search tree contains a node with the given value. Returns True if found, False otherwise.
_contains_recursive function is used for recursive search of a value in the binary search tree.


         a
       /   \
      b      c
     / \    / \
    d  e   f   g


In this visual, we see a at the root of our tree. Each node has only two child nodes. b and c are children of a and d and e are children of b.
