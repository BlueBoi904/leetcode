"""

104. Maximum Depth of Binary Tree
Easy
9K
149
company
Amazon
company
Apple
company
Google
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2


Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
Accepted
2M
Submissions
2.8M
Acceptance Rate
73.2%
Seen this question in a real interview before?
1/4

"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# First attempt, niave approach


def max_depth(root: TreeNode) -> int:
    def dfs(root, depth=0):
        if not root:
            return depth
        return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))

    return dfs(root)


def maxDepth(root: TreeNode):
    if root == None:
        return 0
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    return max(left, right) + 1
