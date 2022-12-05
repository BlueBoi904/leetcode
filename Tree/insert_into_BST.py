"""

701. Insert into a Binary Search Tree
Medium
4.3K
154
company
LinkedIn
company
Amazon
company
Google
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

 

Example 1:


Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:

Example 2:

Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]
Example 3:

Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]
 

Constraints:

The number of nodes in the tree will be in the range [0, 104].
-108 <= Node.val <= 108
All the values Node.val are unique.
-108 <= val <= 108
It's guaranteed that val does not exist in the original BST.

"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Binary Tree =>


"""


A binary tree is a tree data structure in which each node can have a maximum of 2 children.

It means that each node in a binary tree can have either one, or two or no children.
Each node in a binary tree contains data and references to its children.
Both the children are named as left child and the right child according to their position.
The structure of a node in a binary tree is shown in the following figure.


"""

# BST =>


"""


A binary search tree is a binary tree data structure with the following properties.

There are no duplicate elements in a binary search tree.
The element at the left child of a node is always less than the element at the current node.  
The left subtree of a node has all elements less than the current node.
The element at the right child of a node is always greater than the element at the current node.
The right subtree of a node has all elements greater than the current node. 
Following is an example of a binary search tree that satisfies all the properties discussed above.


"""

#


def insert_into_bst(root: TreeNode, val: int):

    pass
