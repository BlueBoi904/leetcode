import math


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node: TreeNode, low=-math.inf, high=math.inf):
            if node is None:
                return True
            if node.val <= low or node.val >= high:
                return False
            return (valid(node.right, node.val, high) and
                    valid(node.left, low, node.val))

        return valid(root)