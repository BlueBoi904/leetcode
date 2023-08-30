# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS solution using queue
class Solution:
    def min_depth(self, root: [TreeNode]) -> int:
        if not root:
            return 0
        queue = [[root, 1]]
        while queue:
            node, count = queue.pop(0)
            if not node.left and not node.right:
                return count
            if node.left:
                queue.append([node.left, count + 1])
            if node.right:
                queue.append([node.right, count + 1])
