"""

226. Invert Binary Tree
Easy
11.7K
<<<<<<< HEAD
162
=======
163
>>>>>>> b1d269a7a7a0e8e5a0a5113738428665e879d5ab
company
Amazon
company
Google
company
Facebook
Given the root of a binary tree, invert the tree, and return its root.

<<<<<<< HEAD

=======
 
>>>>>>> b1d269a7a7a0e8e5a0a5113738428665e879d5ab

Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
<<<<<<< HEAD

=======
 
>>>>>>> b1d269a7a7a0e8e5a0a5113738428665e879d5ab

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
<<<<<<< HEAD
    def invertTree(self, root: [TreeNode]):
        pass
=======
    def maxDepth(self, root: TreeNode) -> int:

        if not root:
            return 0
        elif root.children:
            return 1 + max([self.maxDepth(c) for c in root.children])
        else:
            return
>>>>>>> b1d269a7a7a0e8e5a0a5113738428665e879d5ab
