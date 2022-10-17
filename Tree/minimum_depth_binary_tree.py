"""

111. Minimum Depth of Binary Tree
Easy
5K
1K
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5


Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000

"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        children = [root.left, root.right]
        # if we're at leaf node
        if not any(children):
            return 1

        min_depth = float('inf')
        for c in children:
            if c:
                min_depth = min(self.minDepth(c), min_depth)
        return min_depth + 1


def min_depth(root):
    if not root:
        return 0
    else:
        stack, min_depth = [(1, root), ], float('inf')

    while stack:
        depth, root = stack.pop()
        children = [root.left, root.right]
        if not any(children):
            min_depth = min(depth, min_depth)
        for c in children:
            if c:
                stack.append((depth + 1, c))

    return min_depth
