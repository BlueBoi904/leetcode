"""

257. Binary Tree Paths
Easy
5.4K
231
company
Amazon
company
Capital One
company
Bloomberg
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.



Example 1:


Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
Example 2:

Input: root = [1]
Output: ["1"]

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binaryTreePaths(root: TreeNode):
    # Use dfs
    def construct_paths(root, path):
        if root:
            path += str(root.val)
            if not root.left and not root.right:  # if reach a leaf
                paths.append(path)  # update paths
            else:
                path += '->'  # extend the current path
                construct_paths(root.left, path)
                construct_paths(root.right, path)

    paths = []
    construct_paths(root, '')
    return paths
