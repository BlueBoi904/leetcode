"""



"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        l = root.left
        r = root.right

        def depth(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            if l.val == r.val:
                return depth(l.left, r.right) and depth(l.right, r.left)
            return False
        return depth(l, r)
